from django.urls import path
from .views import *
urlpatterns = [
path('',HomePageView,name='Home'),
path('login', login, name='login'),
path('register', register, name='register'),
path('logout', logout, name='logout'),
path('about', about, name='about'),
path('contact', contact, name='contact'),
path('profile', profile, name='profile'),
path('editprofile', editProfile, name='editprofile'),
path('selectcard',EditCard,name='EditCard'),
path('editcard',SaveEditedCard,name='EditCard'),
path('orderhistory',UserOrderHistory,name='UserOrderHistory'),
]
