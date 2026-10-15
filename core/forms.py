from django import forms
from .models import (
    Categoria,
    Bairro,
    Usuario,
    Denuncia,
    Anexo,
    HistoricoStatus,
    Notificacao
)


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao', 'icone', 'cor']


class BairroForm(forms.ModelForm):
    class Meta:
        model = Bairro
        fields = ['nome', 'descricao']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome',
            'email',
            'cpf',
            'tipo_usuario',
            'ativo'
        ]


class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = [
            'usuario',
            'anonima',
            'descricao',
            'status',
            'prioridade',
            'latitude',
            'longitude',
            'endereco',
            'categoria',
            'bairro',
            'avaliacao'
        ]


class AnexoForm(forms.ModelForm):
    class Meta:
        model = Anexo
        fields = [
            'denuncia',
            'nome_arquivo',
            'caminho_arquivo'
        ]


class HistoricoStatusForm(forms.ModelForm):
    class Meta:
        model = HistoricoStatus
        fields = [
            'denuncia',
            'status_antigo',
            'status_novo',
            'usuario_alteracao',
            'justificativa'
        ]


class NotificacaoForm(forms.ModelForm):
    class Meta:
        model = Notificacao
        fields = [
            'usuario',
            'denuncia',
            'titulo',
            'mensagem',
            'tipo',
            'lida'
        ]
