from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def register(request):
    return render(request,'users/register.html', {'title': 'register'})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error