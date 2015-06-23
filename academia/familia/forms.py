from django import forms
from django.contrib.auth.models import User
from academiaCore.models import UserProfile

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        labels = {
            'email': 'Correo electronico',
            'password': 'Contraseña',
        }

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


    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.data.get("password1"))

        nUserName = "".join(self.data.get("first_name").split() + self.data.get("last_name").split())
        user.username = nUserName[0:40] if (len(nUserName) > 40) else nUserName

        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)
        labels = {
            'first_name': 'Nombre(s) del usuario',
            'last_name':'Apellidos del usuario',
            'email': 'Correo electronico',
        }

class RegisterUserProfileForm(forms.ModelForm):
    def clean(self):
        data = super(RegisterUserProfileForm, self).clean()
        birthday_data = data.get("birthday")
        if not birthday_data:
            msg = "Debe introducir su fecha de nacimiento "
            self.add_error('birthday', msg)

    class Meta:
        model = UserProfile
        fields = {'birthday', 'user_type'}
        labels = {
            'user_type': 'Titulo',
            'birthday': 'Fecha de nacimiento',
        }
