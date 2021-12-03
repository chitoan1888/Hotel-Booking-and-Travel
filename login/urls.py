from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    # url(r'', views.index),
    url(r'', views.trangchu, name='trangchu'),
    url(r'trangchu/', views.trangchu, name='trangchu'),
    url(r'trangchu/login/', views.login_user, name='login'),
    url(r'trangchu/logout/', views.logout_user, name='logout'),
    url(r'trangchu/register/', views.register, name='register'),
    url(r'trangchu/profile/', views.edit_profile, name='profile'),
    url(r'trangchu/change_password/', views.PasswordsChangeView.as_view(template_name='change_password.html')),
    url(r'trangchu/change_success/', views.change_success, name="change_success"),
]