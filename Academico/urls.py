
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCursos/<codigo>', views.edicionCursos),
    path('editarCurso/', views.editarCurso),
    path('eliminarCursos/<codigo>', views.eliminarCurso)
]
