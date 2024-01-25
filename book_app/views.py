from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .models import book_type 
from .models import BookType

# Create your views here.
def home(request):
    return render(request,'base.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
            pass
    return render(request, 'login.html')

def logout_view(request):
        logout(request)
        return redirect('/login')


from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.models import User
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username=username, password=password)
        new_user.save()
        return redirect('/login') 
    return render(request, 'register.html')




def index(request):
    book_types = BookType.objects.all()
    return render(request, 'base.html', {'book_types': book_types})
