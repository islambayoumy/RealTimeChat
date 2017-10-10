from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


User = get_user_model()


@login_required(login_url='log_in/')
def home(request):
    users = User.objects.all()
    return render(request, 'chat/home.html', {'users': users})


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('chat:home'))
        else:
            print(form.errors)
    return render(request, 'chat/log_in.html', {'form': form})


@login_required(login_url='log_in/')
def log_out(request):
    logout(request)
    return redirect(reverse('chat:log_in'))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('chat:log_in'))
        else:
            print(form.errors)
    return render(request, 'chat/sign_up.html', {'form': form})
