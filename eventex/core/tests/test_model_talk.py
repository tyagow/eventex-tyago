from django.test import TestCase

from eventex.core.managers import PeriodManager
from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Titulo da Palestra'
            # start='10:00',
            # description='Descrição da palestra.'
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many speakers"""
        self.talk.speakers.create(
            name='Tiago Almeida',
            slug='tiago-almeida',
            website='http://tyagopartiu.net'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_start_can_be_blank(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_description_can_be_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_can_be_blank(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual(self.talk.title, str(self.talk))


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start='11:59')
        Talk.objects.create(title='Afternoon Talk', start='12:00')

    def test_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)

    def test_at_morning(self):
        """Make sure Manager objects has method at_morning """
        qs = Talk.objects.at_morning()
        expected = ['Morning Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)

    def test_at_afternoon(self):
        """Make sure Manager objects has method at_afternoon """
        qs = Talk.objects.at_afternoon()
        expected = ['Afternoon Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)

