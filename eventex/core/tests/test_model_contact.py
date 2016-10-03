from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name="Tiago Almeida",
            slug='tiago-almeida',
            photo='http://goo.gl/dAVBQm'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,kind=Contact.EMAIL,
                                         value='tyagow@hotmail.com.br'
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,kind=Contact.PHONE,
                                         value='=48-91911234'
        )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind="A", value="B")
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker,kind=Contact.EMAIL,
                                         value='tyagow@hotmail.com.br')
        self.assertEqual('tyagow@hotmail.com.br', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        speaker = Speaker.objects.create(
            name="Tiago Almeida",
            slug='tiago-almeida',
            photo='http://goo.gl/dAVBQm'
        )
        speaker.contact_set.create(kind=Contact.EMAIL, value='tiago@almeida.com')
        speaker.contact_set.create(kind=Contact.PHONE, value='21-2234-2345')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['tiago@almeida.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['21-2234-2345']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)