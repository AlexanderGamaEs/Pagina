from django.shortcuts import render
from django.http import HttpResponseRedirect
from familia.forms import LoginUserForm, RegisterUserForm, RegisterUserProfileForm

def index(request):
    return HttpResponse("Index: En construcción")

def login(request):
    if request.method == 'POST':
        user_form = LoginUserForm(data=request.POST)

        user = authenticate(email=user_form.email, password=user_form.password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user/')
        else:
            print("Invalid login details: {0}, {1}".format(email, password))
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
