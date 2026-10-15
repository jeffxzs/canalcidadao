from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=100)
    cor = models.CharField(max_length=20)

    class Meta:
        db_table = 'categoria'


class Bairro(models.Model):
    id_bairro = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        db_table = 'bairro'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    senha_hash = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    tipo_usuario = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuario'


class Denuncia(models.Model):
    id_denuncia = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        db_column='id_usuario',
        related_name='denuncias'
    )

    anonima = models.BooleanField(default=False)
    descricao = models.TextField()
    status = models.CharField(max_length=50)
    prioridade = models.CharField(max_length=30)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6,
        null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6,
        null=True, blank=True
    )
    endereco = models.CharField(max_length=255)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        db_column='id_categoria',
        related_name='denuncias'
    )

    bairro = models.ForeignKey(
        Bairro,
        on_delete=models.PROTECT,
        db_column='id_bairro',
        related_name='denuncias'
    )

    avaliacao = models.IntegerField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'denuncia'


class Anexo(models.Model):
    id_anexo = models.AutoField(primary_key=True)

    denuncia = models.ForeignKey(
        Denuncia,
        on_delete=models.CASCADE,
        db_column='id_denuncia',
        related_name='anexos'
    )

    nome_arquivo = models.CharField(max_length=255)
    caminho_arquivo = models.CharField(max_length=500)

    class Meta:
        db_table = 'anexo'


class HistoricoStatus(models.Model):
    id_historico = models.AutoField(primary_key=True)

    denuncia = models.ForeignKey(
        Denuncia,
        on_delete=models.CASCADE,
        db_column='id_denuncia',
        related_name='historicos'
    )

    status_antigo = models.CharField(max_length=50)
    status_novo = models.CharField(max_length=50)

    usuario_alteracao = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        db_column='id_usuario_alteracao',
        related_name='alteracoes_status'
    )

    justificativa = models.TextField()
    data_alteracao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'historico_status'


class Notificacao(models.Model):
    id_notificacao = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario',
        related_name='notificacoes'
    )

    denuncia = models.ForeignKey(
        Denuncia,
        on_delete=models.CASCADE,
        db_column='id_denuncia',
        related_name='notificacoes'
    )

    titulo = models.CharField(max_length=150)
    mensagem = models.TextField()
    tipo = models.CharField(max_length=50)
    lida = models.BooleanField(default=False)
    data_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notificacao'
