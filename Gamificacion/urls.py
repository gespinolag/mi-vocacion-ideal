from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('cuestionario/', views.questionary, name='questionary'),
    path('obtener-preguntas/', views.questions, name='obtener-preguntas'),
    path('enviar-resultados/', views.sendResults, name='enviar-resultados'),
    path('resultados/', views.finalResults, name='resultados'),
    path('detalles-de-carreras/', views.careerDetails, name='detalles-de-carreras'),
    path('funcion-de-calculo/', views.aboutCalculationFunction, name='funcion-de-calculo'),
    path('detalles-de-rasgos-de-personalidad/', views.userTraitDetails, name='detalles-de-rasgos-de-personalidad')
]