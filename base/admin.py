from django.contrib import admin
from .models import OcCustomer, OcLead, OcLeadSales
# Register your models here.
admin.site.register(OcCustomer)
admin.site.register(OcLead)
admin.site.register(OcLeadSales)