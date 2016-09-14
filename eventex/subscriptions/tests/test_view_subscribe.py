from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):
	def setUp(self):
		self.resp = self.client.get('/inscricao/')

	def test_get(self):
		"""Get /inscricao/ must return code 200"""
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		"""Must use subscriptions/subscription_form.html"""
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

	def test_html(self):
		"""Html must contain input tags"""
		tags = (('<form', 1),
		        ('<input', 6),
		        ('type="text"', 3),
		        ('type="email"', 1),
		        ('type="submit"', 1))
		for text, count in tags:
			with self.subTest():
				self.assertContains(self.resp, text, count)

	def test_csrf(self):
		self.assertContains(self.resp, 'csrfmiddlewaretoken')

	def test_has_form(self):
		"""Context must have subscription form"""
		form = self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)


class SubscribePostValid(TestCase):
	def setUp(self):
		data = dict(name='Tiago Almeida', cpf='12345678901', email='tyagow@hotmail.com.br', phone='48-9142-0350')
		self.resp = self.client.post('/inscricao/', data)

	def test_post(self):
		"""Valid POST should redirect to /incricao/"""

		self.assertEqual(302, self.resp.status_code)

	def test_send_subscribe_email(self):
		self.assertEqual(1, len(mail.outbox))

	def test_save_subscription(self):
		self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):
	def setUp(self):
		self.response = self.client.post('/inscricao/', {})

	def test_post(self):
		"""invalid POST Should not redirect"""
		self.assertEqual(200, self.response.status_code)

	def test_template(self):
		self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

	def test_has_form(self):
		form = self.response.context['form']
		self.assertIsInstance(form, SubscriptionForm)

	def test_form_has_errors(self):
		form = self.response.context['form']
		self.assertTrue(form.errors)

	def test_dont_save_subscription(self):
		self.assertFalse(Subscription.objects.exists())


class SubscribeSuccessMessage(TestCase):
	def test_message(self):
		data = dict(name='Tiago Almeida', cpf='12345678901', email='tyagow@hotmail.com.br', phone='48-9142-0350')

		response = self.client.post('/inscricao/', data, follow=True)
		self.assertContains(response, 'Inscrição confirmada!')
