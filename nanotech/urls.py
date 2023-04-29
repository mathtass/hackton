from django.urls import path
from . import views


urlpatterns = [
    path('formulario', views.formulario, name='formulario'),
    path('incidentes', views.lista_incidentes, name='incidentes'),]