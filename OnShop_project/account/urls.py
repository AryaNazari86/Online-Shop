from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signout', views.Signout.as_view(), name='signout'),
    path('signin', views.Signin.as_view(), name='signin'),
    path('profile', views.profile, name='profile'),
]