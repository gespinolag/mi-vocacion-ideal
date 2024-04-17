from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('test/', views.test, name='test'),
    path('obtener-preguntas/', views.getQuestions, name='obtener-preguntas'),
    path('enviar-resultados/', views.sendResults, name='enviar-resultados'),
    path('results/', views.finalResults, name='results'),
]