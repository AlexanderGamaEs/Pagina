from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from academiaCore.models import UserProfile

class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(
    	required=True,
    	help_text = "Contraseña",
    	label = "Contraseña",
    	widget=forms.widgets.PasswordInput,
    	max_length=40,)
    password2 = forms.CharField(
    	required=True,
    	help_text = "Contraseña",
    	label = "Confirme su contraseña",
    	widget=forms.widgets.PasswordInput,
    	max_length=40,)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class RegisterUserProfileForm(UserCreationForm):
    class Meta:
    	model = UserProfile
    	fields = {'user_type', 'birthday'}
