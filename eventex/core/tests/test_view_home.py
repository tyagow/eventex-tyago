from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template_index_in_home(self):
        """GET / template must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_list(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

    def test_spakers(self):
        """Must show keynote speakers"""
        contents = [
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'Alan Turing',
            'http://hbn.link/turing-pic'
        ]
        for expected_content in contents:
            with self.subTest():
                self.assertContains(self.response, expected_content)

    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)
