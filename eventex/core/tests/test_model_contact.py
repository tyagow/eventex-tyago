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

    def test_couces(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind="A", value="B")
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker,kind=Contact.EMAIL,
                                         value='tyagow@hotmail.com.br')
        self.assertEqual('tyagow@hotmail.com.br', str(contact))