from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('course',views.course,name='course'),
    path('element',views.element,name='element'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    ]
