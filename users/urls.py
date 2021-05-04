from django.urls import path
# from django.conf.urls import url
from .views import register
# for login and logout functionalities
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name="sign-up"),
    path('login/',
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'),


]