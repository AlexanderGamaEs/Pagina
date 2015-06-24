from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from familia.forms import LoginUserForm, RegisterUserForm, RegisterUserProfileForm

def index(request):
    if not request.user.is_authenticated():
        return user_login(request)
    
    return HttpResponse("Index: En construcción " + request.user.get_username() + "<a href='logout/''><p>Cerrar sesión</p></a>")

def user_login(request):
    if request.method == 'POST':
        user_form = LoginUserForm(data=request.POST)

        if user_form.is_valid(): 
            print(user_form.data.get('emailLog'))
            userWithEmail = User.objects.get(email=user_form.data.get('emailLog')) #En la funcion cleaned la forma se comprobo que existiera el usuario
            user = authenticate(username=userWithEmail, password=user_form.data.get('passwordLog'))
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/familia/')
            else:
                return HttpResponse("Datos de inicio invalidos")
        else:
        	print(user_form.errors)
        	return render(request, 'core/login.htm', {'user_form': user_form})
    else:
        user_form = LoginUserForm()
        return render(request, 'core/login.htm', {'user_form': user_form})

def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('familia'))


def user_register(request):
    registered = False

    if request.method == 'POST':
        user_form = RegisterUserForm(data=request.POST)
        profile_form = RegisterUserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            #if 'pic' in request.FILES:
            #    profile.pic = request.FILES['pic']

            profile.save()

            registered = True
            return HttpResponseRedirect('/user/')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = RegisterUserForm()
        profile_form = RegisterUserProfileForm()

    return render(request,
            'core/register.htm',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
