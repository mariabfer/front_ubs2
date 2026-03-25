from django.contrib import admin
from .models import Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'number', 'city', 'state', 'cep']

admin.site.register(Address, AddressAdmin)

