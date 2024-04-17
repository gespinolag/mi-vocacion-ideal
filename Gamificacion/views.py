from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Diccionario de carreras
careers = {
    'Economía': ['Apertura a la experiencia', 'Conciencia', 'Amabilidad', 'Extraversión'],
    'Contador Público Nacional': ['Conciencia', 'Amabilidad'],
    'Derecho': ['Conciencia', 'Amabilidad', 'Extraversión'],
    'Notariado': ['Conciencia', 'Amabilidad'],
    'Medicina': ['Conciencia', 'Amabilidad', 'Neuroticismo'],
    'Enfermería': ['Amabilidad', 'Neuroticismo'],
    'Odontología': ['Conciencia', 'Amabilidad'],
    'Kinesiología y Fisioterapia': ['Amabilidad', 'Extraversión', 'Conciencia'],
    'Bioquímica': ['Apertura a la experiencia', 'Conciencia', 'Amabilidad'],
    'Química y Farmacia': ['Conciencia', 'Amabilidad'],
    'Psicología': ['Amabilidad', 'Conciencia'],
    'Ingeniería Informática': ['Apertura a la experiencia', 'Conciencia', 'Extraversión'],
    'Ingeniería Industrial': ['Apertura a la experiencia', 'Conciencia', 'Extraversión'],
    'Ingeniería Química': ['Apertura a la experiencia', 'Conciencia', 'Amabilidad']
}

# Preguntas
questions = [
    "¿Te gustan las actividades creativas como escribir o pintar?",
    "¿Te sientes a gusto al conversar con personas que tienen ideas y experiencias diferentes a las tuyas?",
    "¿Te gusta explorar nuevas ideas y conceptos?",
    "¿Eres adaptable a nuevas situaciones y cambios en tu vida?",
    "¿Te gusta experimentar con nuevas tecnologías y aplicaciones?",
    "¿Eres curioso/a acerca de cómo funcionan las cosas en el mundo?",
    "¿Te consideras una persona organizada en tus actividades diarias?",
    "¿Te molesta cuando las cosas no se hacen bien y a tiempo?",
    "¿Eres exigente con tus actividades?",
    "¿Te esfuerzas por seguir reglas y normas establecidas?",
    "¿Prefieres completar tus tarea antes de disfrutar de un descanso?",
    "¿Te consideras una persona en la que los demás pueden confiar?",
    "¿Te desenvuelves fácilmente en situaciones sociales?",
    "¿Participas en actividades grupales o trabajas en equipo?",
    "¿Sientes incomodidad al interactuar con personas que acabas de conocer?",
    "¿Te gusta ser el centro de atención en situaciones sociales?",
    "¿Los demás te consideran por ser extrovertido/a y comunicativo/a en diferentes contextos?",
    "¿Disfrutas asistir a eventos sociales como fiestas o reuniones?",
    "¿Dedicas tu tiempo para ayudar a los demás?",
    "¿Eres capaz de entender los sentimientos de otras personas?",
    "¿Evitas involucrarte en conflictos y prefieres la armonía?",
    "¿Te esfuerzas por ser amable y cortés con los demás?",
    "¿Te gusta realizar actos de bondad sin esperar recompensa?",
    "¿Te preocupas por el bienestar de los demás?",
    "¿Sientes emociones negativas en demasía como preocupación o ansiedad?", 
    "¿Te resulta difícil controlar tus emociones?",
    "¿Te irritas fácilmente ante los cambios inesperados?",
    "¿Tienes preocupación en exceso por situaciones pequeñas?",
    "¿Te afectan mucho las críticas o comentarios negativos?",
    "¿Te consideras alguien que necesita apoyo emocional en momentos difíciles?"
]

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

def test(request):
    request.session['values_list'] = []
    return render(request, 'questionary.html', {})

def getQuestions(request):
    return JsonResponse({'questions': questions})

@csrf_exempt
def sendResults(request):
    if request.method == 'POST':
        value = int(request.POST.get('value'))
        divisionSize = 6
        values_list = request.session.get('values_list', [])
        values_list.append(value)
        request.session['values_list'] = values_list
        subarrays = [values_list[i:i+divisionSize] for i in range(0, len(values_list), divisionSize)]
        sums = [sum(subarray) for subarray in subarrays]
        # sums_array = list(sums)
        # print(subarrays)
        # print(sums_array)
        request.session['sums_array'] = sums
        return JsonResponse({'message': 'Valor recibido'}, status=200)

    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

# Definir rangos de puntajes para cada rasgo de personalidad
traitScoreRanges = {
    "Apertura a la experiencia": {
        "Muy Alto": (81, 100),
        "Alto": (61, 80),
        "Medio": (41, 60),
        "Bajo": (21, 40),
        "Muy Bajo": (0, 20)
    },
    "Conciencia": {
        "Muy Alto": (81, 100),
        "Alto": (61, 80),
        "Medio": (41, 60),
        "Bajo": (21, 40),
        "Muy Bajo": (0, 20)
    },
    "Extraversión": {
        "Muy Alto": (81, 100),
        "Alto": (61, 80),
        "Medio": (41, 60),
        "Bajo": (21, 40),
        "Muy Bajo": (0, 20)
    },
    "Amabilidad": {
        "Muy Alto": (81, 100),
        "Alto": (61, 80),
        "Medio": (41, 60),
        "Bajo": (21, 40),
        "Muy Bajo": (0, 20)
    },
    "Neuroticismo": {
        "Muy Alto": (81, 100),
        "Alto": (61, 80),
        "Medio": (41, 60),
        "Bajo": (21, 40),
        "Muy Bajo": (0, 20)
    }
}

def categorizeResults(sumsArray, rasgosNames):
    results = {}

    for i in range(len(sumsArray)):
        rasgo = rasgosNames[i]
        score = sumsArray[i]
        maxPoint = len(questions)  # Máximo puntaje posible por rasgo

        if rasgo in traitScoreRanges:
            ranges = traitScoreRanges[rasgo]
            porcentaje = (score / maxPoint) * 100

            for category, (lower, upper) in ranges.items():
                if lower <= porcentaje <= upper:
                    results[rasgo] = category
                    break

    return results


def categorizeResultss(sumsArray, rasgosNames):
    results = {}
    maxPoint = len(questions)
    for i in range(len(sumsArray)):
        porcentaje = (sumsArray[i] / maxPoint) * 100
        rasgo = rasgosNames[i] 
        results[rasgo] = f"{porcentaje:.0f}%"
    return results

def careerSelection(userResults):
    selectedCareers = []
    thresholdPercentage = 30 

    # Diccionario para mapear categorías de puntajes a valores numéricos
    scoreMapping = {
        'Bajo': 20,
        'Medio - Bajo': 40,
        'Medio': 60,
        'Medio - Alto': 80,
        'Alto': 100
    }

    for career, requiredTraits in careers.items():
        matchCount = 0
        totalTraits = len(requiredTraits)

        for trait in requiredTraits:
            if trait in userResults:
                userCategory = userResults[trait]
                if userCategory in scoreMapping:
                    userPercentage = scoreMapping[userCategory]
                    if trait in traitScoreRanges and userCategory in traitScoreRanges[trait]:
                        lower, upper = traitScoreRanges[trait][userCategory]
                        if lower <= userPercentage <= upper:
                            matchCount += 1
        
        if totalTraits > 0:
            matchPercentage = (matchCount / totalTraits) * 100
        else:
            matchPercentage = 0
        
        if matchPercentage >= thresholdPercentage:
            selectedCareers.append(career)
    
    return selectedCareers


def finalResults(request):
    sumsArray = request.session.get('sums_array', [])
    rasgosNames = ["Apertura a la experiencia", "Conciencia", "Extraversión", "Amabilidad", "Neuroticismo"]
    userResults = categorizeResults(sumsArray, rasgosNames)
    userResultss = categorizeResultss(sumsArray, rasgosNames)
    print("Suma de los puntajes por rasgo: ", sumsArray)
    print(userResults)
    print(userResultss)
    careerSuggestion = careerSelection(userResults)
    context = {
        'careerSuggestion': careerSuggestion
    }
    
    print("Carreras sugeridas basadas en los resultados de personalidad:")
    if careerSuggestion:
        for career in careerSuggestion:
            print("- " + career)
    else:
        print("No se encontraron carreras que coincidan con los resultados de personalidad.")

    return render(request, 'results.html', context)
