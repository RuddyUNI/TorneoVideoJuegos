from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('hello/<str:username>',views.depuesindex),
    path('torneo',views.torneo),
    path('super_smash_bros',views.super_smash_bros),
    path('fifa',views.fifa),
    path('call_of_duty',views.call_of_duty)

]