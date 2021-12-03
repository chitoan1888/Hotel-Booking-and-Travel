from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #Chi tiết
    path(r'', views.cn_detail, name="cn_detail"),

    #MList Miền Bắc
    path(r'MienBac/', views.cn_mienbac, name="cn_mienbac"),
    path(r'MienBac/LaoCai/', views.cn_laocai, name="cn_laocai"),
    path(r'MienBac/HaNoi/', views.cn_hanoi, name="cn_hanoi"),

    #List Miền Nam
    path(r'MienNam/', views.cn_miennam, name="cn_miennam"),
    path(r'MienNam/VungTau/', views.cn_vungtau, name="cn_vungtau"),

    #List Miền Trung
    path(r'MienTrung/Hue/', views.cn_hue, name="cn_hue"),
    path(r'MienTrung/', views.cn_mientrung, name="cn_mientrung"),

    
    
]
