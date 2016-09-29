from django.shortcuts import resolve_url
from django.test import TestCase
from eventex.core.models import Speaker


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='http://hbn.link/hopper-pic',
            website='http://hbn.link/hopper-site',
            description='Programadora e Almirante.'
        )

    def test_create(self):
        self.assertTrue(Speaker.objects.exists())

    def test_description_can_be_blank(self):
        field = Speaker._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_website_can_be_blank(self):
        field = Speaker._meta.get_field('website')
        self.assertTrue(field.blank)

    def test_str(self):
        '''Make sure name field is the representation as string of the model'''
        self.assertEqual(self.speaker.name, str(self.speaker))

    def test_get_absolute_url(self):
        url = resolve_url('speaker_detail', slug=self.speaker.slug)
        self.assertEqual(url, self.speaker.get_absolute_url())
