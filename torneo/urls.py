from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello/<str:username>', views.depuesindex),
    path('torneo', views.torneo),
    path('super_smash_bros', views.super_smash_bros),
    path('fifa', views.fifa),
    path('call_of_duty', views.call_of_duty),
    path('accounts/login/eventos', views.eventos),  
    path('agregar_evento/', views.agregar_eventos, name='agregar_evento'),
    path('confirmacion_registro/', views.confirmacion_registro, name='confirmacion_registro')
]
