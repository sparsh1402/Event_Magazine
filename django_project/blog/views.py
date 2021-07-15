from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


 
        

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
         post = self.get_object()
         if self.request.user == post.author:
            return True
         return False

   

def contact_us(request):
    if request.method == "POST":
        head_name = request.POST['head-name']
        phone_number = request.POST['phone-number']
        society_name = request.POST['society-name']
        society_email = request.POST['society-email']
        message = request.POST['message']
        
        msg = "Head Name : " + head_name + "\n" + "Phone Number : " + phone_number + "\n"  + "Society Name: " + society_name +"\n" + "Society Email: " + society_email +"Message" + "\n" + message 
              
        

        

        send_mail(
          "Registration",
        msg,
        society_email,
          ['ishu142000@gmail.com']
            )
    return render(request, 'blog/contact_us.html',{'title' : 'contact_us'})   

def about(request):
    return render(request, 'blog/about.html',{'title' : 'about'}) 




  