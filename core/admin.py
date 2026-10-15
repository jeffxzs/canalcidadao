from django.contrib import admin
from .models import (
    Categoria,
    Bairro,
    Usuario,
    Denuncia,
    Anexo,
    HistoricoStatus,
    Notificacao
)

admin.site.register(Categoria)
admin.site.register(Bairro)
admin.site.register(Usuario)
admin.site.register(Denuncia)
admin.site.register(Anexo)
admin.site.register(HistoricoStatus)
admin.site.register(Notificacao)

# Register your models here.
