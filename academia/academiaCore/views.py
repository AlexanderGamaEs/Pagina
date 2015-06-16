from django.shortcuts import render
from academiaCore.forms import RegisterUserForm

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print(form.errors)
    else:
        form = RegisterUserForm()
    return render(request, 'core/register.htm', {'form': form})