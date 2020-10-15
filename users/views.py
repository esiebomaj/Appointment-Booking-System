from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.


def register_view(request):
    print('hello there')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/')

    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
