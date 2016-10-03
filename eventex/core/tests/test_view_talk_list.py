from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Talk, Speaker, Course


class TalkListGet(TestCase):
    def setUp(self):
        t1 = Talk.objects.create(title='Título da Palestra', start='10:00',
             description='Descrição da palestra.')
        t2 = Talk.objects.create(title='Título da Palestra', start='13:00',
             description='Descrição da palestra.')
        c1 = Course.objects.create(title='Título do Curso', start='09:00',
             description='Descrição do curso.', slots=20)
        speaker = Speaker.objects.create(
            name='Tiago Almeida',
            slug='tiago-almeida',
            website='http://tyagopartiu.net'
        )
        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        c1.speakers.add(speaker)
        self.response = self.client.get(r('talk_list'))


    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Título da Palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (3, '/palestrantes/tiago-almeida'),
            (3, 'Tiago Almeida'),
            (2, 'Descrição da palestra'),
            (1, "Título do Curso"),
            (1, "09:00"),
            (1, "Descrição do curso."),
        ]
        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected, count)

    def test_context(self):
        variables = ['morning_talks', 'afternoon_talks', 'courses']
        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)


class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(r('talk_list'))

        self.assertContains(response, 'Ainda não existem palestras de manhã.')
        self.assertContains(response, 'Ainda não existem palestras de tarde.')