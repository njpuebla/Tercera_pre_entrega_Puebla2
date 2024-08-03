from django.urls import path
from app import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path('electricas/', views.electricas, name='Electricas'),
    path('acusticas/', views.acusticas, name='Acusticas'),
    path('amplificadores/', views.amplificadores, name='Amplificadores'),
    path('efectos/', views.efectos, name='Efectos'),
    path('buscar-electricas/', views.buscar_electricas, name="Buscar_Electricas"),
]