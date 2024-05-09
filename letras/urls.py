from django.urls import path
from letras import views

urlpatterns = [
    
    path('', views.Home),
    path('saludo', views.saludo),
    path('presentacion', views.presentacion),
    path('decripcion', views.descripcion),
    
]
