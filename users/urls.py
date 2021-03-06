from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    
    path('dashboard', views.Dashboard, name="dashboard"),

    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
