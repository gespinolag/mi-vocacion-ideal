from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    if request.method == "POST" and "btnStartNow" in request.POST:
        return redirect('registration')
    else:
        return render(request, 'home.html')

def registration(request):
    if request.method == "POST" and "registrateBtn" in request.POST:
        return redirect('/test/')
    else:
        return render(request, 'registration.html')

def test(resquest):
    return render(resquest, 'questionary.html')

def getQuestions(resquet):
    questions = [
        "¿Te gustan las actividades creativas como escribir o pintar?",
        "¿Prefieres tener la misma rutina de siempre en vez de probar cosas nuevas?",
        "¿Te gusta explorar nuevas ideas y conceptos?",
        "¿Te consideras una persona organizada en tus actividades diarias?",
        "¿Te molesta cuando las cosas no se hacen bien y a tiempo?",
        "¿Eres exigente con tus actividades?",
        "¿Te desenvuelves fácilmente en situaciones sociales?",
        "¿Participas en actividades grupales o trabajas en equipo?",
        "¿Sientes incomodidad al interactuar con personas que acabas de conocer?",
        "¿Dedicas tu tiempo para ayudar a los demás?",
        "¿Eres capaz de entender los sentimientos de otras personas?",
        "¿Evitas involucrarte en conflictos y prefieres la armonía?",
        "¿Sientes emociones negativas en demasía como preocupación o ansiedad?",
        "¿Te irritas fácilmente ante los cambios inesperados?",
        "¿Tienes preocupación en exceso por situaciones pequeñas?"
    ]
    return JsonResponse({'questions': questions})