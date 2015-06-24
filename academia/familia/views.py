from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginUser
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from familia.forms import LoginUserForm, RegisterUserForm, RegisterUserProfileForm

def index(request):
    if not request.user.is_authenticated():
        return login(request)
    
    return HttpResponse("Index: En construcción " + request.user.get_username())

def login(request):
    if request.method == 'POST':
        user_form = LoginUserForm(data=request.POST)

        email = user_form.data.get('emailLog')
        print()
        print(email)
        print()
        userWithEmail = User.objects.get(email=email)
        user = authenticate(username=userWithEmail, password=user_form.data.get('passwordLog'))

        if user:
            if user.is_active:
                loginUser(request, user)
                return HttpResponseRedirect('/familia/')
        else:
            print("Invalid login details: {0}".format(userWithEmail))
            return HttpResponse("Invalid login details supplied.")
    else:
        user_form = LoginUserForm()
        return render(request, 'core/login.htm', {'user_form': user_form})


def register(request):
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
