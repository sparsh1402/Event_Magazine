from django.shortcuts import render
from .models import Post



# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)
def contact_us(request):
    return render(request, 'blog/contact_us.html',{'title' : 'contact_us'})   
