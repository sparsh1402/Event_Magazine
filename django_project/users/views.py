from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def register(request):
    return render(request,'users/register.html', {'title': 'register'})


# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error