from django.contrib import admin
from main.models import SectionMainPage

class SectionMainPageAdmin(admin.ModelAdmin):
    fields = ('user_type', 'birthday')

admin.site.register(SectionMainPage, SectionMainPageAdmin)
