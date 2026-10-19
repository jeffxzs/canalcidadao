from django.test import TestCase
from django.urls import reverse

from .models import Bairro, Categoria


class CategoriaCRUDTests(TestCase):
    def test_lista_exibe_categorias_em_ordem_alfabetica(self):
        Categoria.objects.create(nome='Zeladoria', descricao='Serviços urbanos', icone='tool', cor='#000000')
        Categoria.objects.create(nome='Iluminação', descricao='Luzes públicas', icone='light', cor='#ffffff')

        response = self.client.get(reverse('categoria_lista'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Iluminação')
        self.assertContains(response, 'Zeladoria')
        self.assertLess(response.content.index('Iluminação'.encode()), response.content.index('Zeladoria'.encode()))

    def test_cadastro_cria_categoria(self):
        response = self.client.post(reverse('categoria_cadastro'), {
            'nome': 'Limpeza',
            'descricao': 'Limpeza urbana',
            'icone': 'brush',
            'cor': '#123456',
        })

        self.assertRedirects(response, reverse('categoria_lista'))
        self.assertTrue(Categoria.objects.filter(nome='Limpeza').exists())

    def test_edicao_atualiza_categoria(self):
        categoria = Categoria.objects.create(nome='Antiga', descricao='Descrição', icone='tag', cor='#000000')

        response = self.client.post(reverse('categoria_editar', args=[categoria.pk]), {
            'nome': 'Nova',
            'descricao': 'Atualizada',
            'icone': 'star',
            'cor': '#ffffff',
        })

        self.assertRedirects(response, reverse('categoria_lista'))
        categoria.refresh_from_db()
        self.assertEqual(categoria.nome, 'Nova')
        self.assertEqual(categoria.descricao, 'Atualizada')

    def test_remocao_exclui_categoria(self):
        categoria = Categoria.objects.create(nome='Temporária', descricao='Descrição', icone='tag', cor='#000000')

        response = self.client.post(reverse('categoria_remover', args=[categoria.pk]))

        self.assertRedirects(response, reverse('categoria_lista'))
        self.assertFalse(Categoria.objects.filter(pk=categoria.pk).exists())


class BairroCRUDTests(TestCase):
    def test_lista_exibe_bairros_em_ordem_alfabetica(self):
        Bairro.objects.create(nome='Vila Nova', descricao='Zona norte')
        Bairro.objects.create(nome='Aldeota', descricao='Zona leste')

        response = self.client.get(reverse('bairro_lista'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Aldeota')
        self.assertContains(response, 'Vila Nova')
        self.assertLess(response.content.index('Aldeota'.encode()), response.content.index('Vila Nova'.encode()))

    def test_cadastro_cria_bairro(self):
        response = self.client.post(reverse('bairro_cadastro'), {
            'nome': 'Centro',
            'descricao': 'Região central',
        })

        self.assertRedirects(response, reverse('bairro_lista'))
        self.assertTrue(Bairro.objects.filter(nome='Centro').exists())

    def test_edicao_atualiza_bairro(self):
        bairro = Bairro.objects.create(nome='Antigo', descricao='Descrição antiga')

        response = self.client.post(reverse('bairro_editar', args=[bairro.pk]), {
            'nome': 'Novo',
            'descricao': 'Descrição atualizada',
        })

        self.assertRedirects(response, reverse('bairro_lista'))
        bairro.refresh_from_db()
        self.assertEqual(bairro.nome, 'Novo')
        self.assertEqual(bairro.descricao, 'Descrição atualizada')

    def test_remocao_exclui_bairro(self):
        bairro = Bairro.objects.create(nome='Temporário', descricao='Descrição')

        response = self.client.post(reverse('bairro_remover', args=[bairro.pk]))

        self.assertRedirects(response, reverse('bairro_lista'))
        self.assertFalse(Bairro.objects.filter(pk=bairro.pk).exists())
