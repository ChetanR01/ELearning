from django.contrib import admin
from .models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name','type','subject']
    search_fields =  ['name','type','subject']
    list_filter = ('type','date')
admin.site.register(Registration, RegistrationAdmin)