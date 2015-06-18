from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from academiaCore.models import UserProfile

class LoginUserForm(forms.ModelForm):
	class Meta:
        model = User
        fields = ('email', 'password')

class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(
        required=True,
        label = "Contraseña",
        widget=forms.widgets.PasswordInput,
        max_length=40,)
    password2 = forms.CharField(
        required=True,
        label = "Confirme su contraseña",
        widget=forms.widgets.PasswordInput,
        max_length=40,)

    def clean(self):
        data = super(RegisterUserForm, self).clean()
        password1_data = data.get("password1")
        password2_data = data.get("password2")

        if not (password1_data and password2_data) and password1_data != password2_data:
            msg = "Las contraseñas no coinciden"
            self.add_error('password1', msg)
            self.add_error('password2', msg)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class RegisterUserProfileForm(forms.ModelForm):
    def clean(self):
        data = super(RegisterUserProfileForm, self).clean()
        birthday_data = data.get("birthday")
        if not birthday_data:
            msg = "Debe introducir su fecha de nacimiento "
            self.add_error('birthday', msg)

    class Meta:
        model = UserProfile
        fields = {'user_type', 'birthday'}
        labels = {
            'user_type': 'Titulo',
            'birthday': 'Fecha de nacimiento',
        }
