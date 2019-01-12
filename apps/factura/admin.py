from django.contrib import admin
from apps.factura.models import Pago, Factura
# Register your models here.
admin.site.register(Pago)
admin.site.register(Factura)