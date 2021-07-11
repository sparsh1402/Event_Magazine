from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('contact_us/', views.contact_us, name = 'blog-contact_us'),
    path('about/', views.about, name = 'blog-about'),

]