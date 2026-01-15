# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('library/', views.library, name='library'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('prevention/', views.prevention, name='prevention'),
    path('contact/', views.contact, name='contact'),
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]