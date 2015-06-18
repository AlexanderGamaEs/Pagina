from django.contrib import admin
from django.contrib.auth.models import User
from academiaCore.models import UserProfile

class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'password')

class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user_type', 'birthday')

admin.site.register(UserProfile, UserProfileAdmin)