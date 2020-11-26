from django.contrib import admin
from .models import usuario, destino, registro
from .forms import destinoForm
# Register your models here.


admin.site.register(usuario)
admin.site.register(destino)
admin.site.register(registro)
