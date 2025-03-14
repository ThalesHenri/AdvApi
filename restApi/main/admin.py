from django.contrib import admin
from .models import Cliente, Advogado, Processo

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Advogado)
admin.site.register(Processo)