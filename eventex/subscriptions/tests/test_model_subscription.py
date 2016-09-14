from _datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Tiago Almeida',
			cpf='00839433333',
			email='tyagow@hotmail.com.br',
			phone='48-91420000',
		)
		self.obj.save()

	def test_create(self):
		self.assertTrue(Subscription.objects.exists())

	def test_created_at(self):
		"""Subscription must have an auto created_at attr."""
		self.assertIsInstance(self.obj.created_at, datetime)
