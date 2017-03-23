from django.contrib import admin
from candidateManager.models import *
# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'state',)
    list_filter = ('state',)
    

admin.site.register(Location, LocationAdmin)
admin.site.register(Notes)