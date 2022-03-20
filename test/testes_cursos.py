from rest_framework import status
from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse


class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1',
            descricao='Curso teste 1',
            nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2',
            descricao='Curso teste 2',
            nivel='A'
        )

    # def test_falhador(self):
    #     self.fail('Teste para falhar de propósito.')

    def test_requisicao_get_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_criar_curso(self):
        """Teste para verificar a requisição POST para criar curso"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'A'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
