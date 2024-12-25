from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'users/htmls/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Kullanıcıyı otomatik olarak giriş yap
            return redirect('home')  # Ana sayfaya yönlendir
        return render(request, 'users/htmls/register.html', {'form': form})

class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'users/htmls/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Başarılı giriş sonrası ana sayfaya yönlendir
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'users/htmls/login.html', {'form': form})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')  # Çıkış yapılınca ana sayfaya yönlendir