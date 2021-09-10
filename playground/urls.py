from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('profile/<int:user>/',views.profile,name='profile'),
    path('cities/<str:id_city>/',views.city,name='city'),
    path('busqueda/',views.busc,name='busqueda'),
    path('busqueda1/',views.busc1,name='busqueda1')
]