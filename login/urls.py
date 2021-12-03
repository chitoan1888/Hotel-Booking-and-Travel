from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    # url(r'', views.index),
    url(r'login/', views.login_user, name='login'),
    url(r'logout/', views.logout_user, name='logout'),
    url(r'register/', views.register, name='register'),
    url(r'profile/', views.edit_profile, name='profile'),
    url(r'change_password/', views.PasswordsChangeView.as_view(template_name='change_password.html')),
    url(r'change_success/', views.change_success, name="change_success"),
]