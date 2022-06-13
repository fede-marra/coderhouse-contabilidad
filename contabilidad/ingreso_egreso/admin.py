from django.contrib import admin
from ingreso_egreso.models import personas, ingresos, egresos, tipo_egreso

# Register your models here.

admin.site.register(personas)
admin.site.register(ingresos)
admin.site.register(egresos)
admin.site.register(tipo_egreso)
