from django.urls import path, include
from . import views


urlpatterns = [
    #finales
    path('', views.inicio, name="inicio"),
    path('juego_unity/', views.juego_unity, name="juego_unity"),
    path('cuenta_usuario',views.cuenta_usuario, name = 'cuenta_usuario'),

    path('grafica1/', views.grafica1, name="grafica1"),

    path('proceso',views.proceso, name = 'proceso'),
    path('datos',views.datos, name = 'datos'),
    path('iniciar_sesion/', views.iniciar_sesion, name="iniciar_sesion"),
    path('buscaJugadorBody', views.buscaJugadorBody, name='buscaJugadorBody'),
    path('ejemploSQL', views.ejemploSQL, name='ejemploSQL'),
    path('score',views.score, name = 'score'),
    path('level',views.Level, name = 'level'),
    path('grafica',views.grafica, name = 'grafica'),

    #ejemplos clase
    path('index2',views.index2, name = 'index2'),
    path('proceso2',views.proceso2, name = 'proceso2')
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

