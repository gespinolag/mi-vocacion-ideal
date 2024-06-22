from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('test/', views.test, name='test'),
    path('obtener-preguntas/', views.getQuestions, name='obtener-preguntas'),
    path('enviar-resultados/', views.questionsResults, name='enviar-resultados'),
    path('results/', views.finalResults, name='results'),
    path('detalles-de-carreras/', views.careerDetails, name='detalles-de-carreras'),
    path('funcion-de-calculo/', views.aboutCalculationFunction, name='funcion-de-calculo')
]