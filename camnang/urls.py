from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'camnang/mientrung/hue/', views.cn_hue, name="cn_hue"),
    url(r'camnang/miennam/vungtau/', views.cn_vungtau, name="cn_vungtau"),
]
