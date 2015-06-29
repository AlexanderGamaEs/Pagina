from django.contrib import admin
from main.models import SectionMainPage

class SectionMainPageAdmin(admin.ModelAdmin):
    fields = ('name', 'content', 'last_edition')

admin.site.register(SectionMainPage, SectionMainPageAdmin)
