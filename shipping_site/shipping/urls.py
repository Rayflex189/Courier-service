from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('price/', views.price, name='price'),
    path('qoute/', views.qoute, name='qoute'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]
