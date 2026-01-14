from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('library/', views.library, name='library'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('prevention/', views.prevention, name='prevention'),
    path('contact/', views.contact, name='contact')
]