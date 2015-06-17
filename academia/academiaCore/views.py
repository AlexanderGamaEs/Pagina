from django.shortcuts import render
from academiaCore.forms import LoginUserForm, RegisterUserForm, RegisterUserProfileForm

def login(request):
    if request.method == 'POST':
    	user_form = LoginUserForm(data=request.POST)

        user = authenticate(username=user_form.username, password=user_form.password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user/')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
    	user_form = LoginUserForm()
        return render(request, 'user/login.htm', {'user_form': user_form})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = RegisterUserForm(data=request.POST)
        profile_form = RegisterUserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

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