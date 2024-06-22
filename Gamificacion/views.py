from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
import random

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

careersInformation = [
    {
        "carrera": "Economía",
        "titulo": "Licenciado en Economía",
        "duracion": "5 años",
        "descripcion": "El licenciado en Economía es un experto en ciencias económicas con formación académica y técnica, "
            "capaz de analizar y asesorar en economía a nivel nacional e internacional, con un enfoque ético y compromiso con el desarrollo social. "
            "Está preparado para tomar decisiones económicas importantes y para continuar su formación en estudios superiores.",
        "img": "/static/img/avatar-carreras/economia-avatar.png"
    },
    {
        "carrera": "Contador Público Nacional",
        "titulo": "Contador Público Nacional",
        "duracion": "4 años",
        "descripcion": "El Contador Público Nacional está formado ética y críticamente en contabilidad y ciencias económicas, preparado para resolver problemas complejos, "
            "aprender continuamente y liderar en entornos organizacionales a nivel local e internacional, en áreas como finanzas, fiscalidad, auditoría y responsabilidad social y ambiental.",
        "img": "/static/img/avatar-carreras/contador-avatar.png"
    },
    {
        "carrera": "Derecho",
        "titulo": "Abogado/a",
        "duracion": "5 años",
        "descripcion": "El abogado está capacitado en ciencias jurídicas para interpretar y aplicar el Derecho, y puede trabajar en la función pública, "
            "ejercer la abogacía o ser Consultor Jurídico en el sector público, privado o mixto.",
        "img": "/static/img/avatar-carreras/derecho-avatar.png"
    },
    {
        "carrera": "Notariado",
        "titulo": "Notario",
        "duracion": "4 años",
        "descripcion": "El notario es un profesional en ciencias jurídicas, especializado en derecho notarial y asistencia jurídica, "
            "capacitado para trabajar en registros públicos, la función pública y como consultor jurídico en diversos sectores.",
        "img": "/static/img/avatar-carreras/notariado-avatar.png"
    },
    {
        "carrera": "Medicina",
        "titulo": "Médico Cirujano",
        "duracion": "7 años",
        "descripcion": "El egresado de la carrera de Medicina es un profesional generalista del área de la salud, capacitado para atender las necesidades de salud prevalentes "
            "y las urgencias no derivables de la población, con principios éticos, sentido de responsabilidad social y comprometido para gerenciar su formación médica continua.",
        "img": "/static/img/avatar-carreras/medicina-avatar.png"
    },
    {
        "carrera": "Enfermería",
        "titulo": "Licenciado/a en Enfermería",
        "duracion": "4 años",
        "descripcion": "El egresado de la carrera de Enfermería podrá identificar y resolver problemas de salud, ejercer como enfermero generalista o especializado, "
            "promover la salud pública y administrar servicios de enfermería, optimizando los recursos disponibles.",
        "img": "/static/img/avatar-carreras/enfermeria-avatar.png"
    },
    {
        "carrera": "Odontología",
        "titulo": "Odontólogo/a",
        "duracion": "5 años",
        "descripcion": "El egresado de la carrera de Odontología es un profesional capacitado para prevenir, diagnosticar, tratar y recuperar la salud bucal del individuo "
            "con calidad y calidez, aplicando principios científicos, éticos, socio humanísticos y capaz de gerenciar su formación contínua.",
        "img": "/static/img/avatar-carreras/odontologia-avatar.png"
    },
    {
        "carrera": "Kinesiología y Fisioterapia",
        "titulo": "Licenciado en Kinesiología y Fisioterapia",
        "duracion": "5 años",
        "descripcion": "El Kinesiólogo Fisioterapeuta podrá desarrollar las actividades dependiendo donde esté, con las competencias y habilidades "
            "para una remuneración adecuada a la formación profesional recibida. Puede desempeñarse en áreas de la salud del ámbito público y privado "
            "como hospitales y centros de salud, centros de rehabilitación y recuperación, centros de investigaciones científicas. Asimismo en el área de deportes "
            "cómo organizaciones deportivas, preparación psico- física y orientación y supervisores de gimnasios.",
        "img": "/static/img/avatar-carreras/kinesiologia-avatar.png"
    },
    {
        "carrera": "Bioquímica",
        "titulo": "Bioquímico/a",
        "duracion": "5 años",
        "descripcion": "El bioquímico es un profesional con sólidos conocimientos científicos,  prácticos y éticos con una formación integral cristiana, "
            "que le permitirá desarrollar sus actividades en el ámbito de la salud y la investigación, en el contexto nacional e internacional. El mismo será capaz de diseñar, "
            "ejecutar, científica, técnica y éticamente pruebas de laboratorio basadas en métodos físicos, químicos y biológicos, a partir de muestras clínicas, toxicológicas, "
            "forenses, alimentarias y biotecnológicas. Además, puede ejercer la dirección técnica de un laboratorio, también manejar con criterios de bioseguridad materiales "
            "peligrosos de origen biológico, radiactivo y químico.",
        "img": "/static/img/avatar-carreras/bioquimica-avatar.png"
    },
    {
        "carrera": "Química y Farmacia",
        "titulo": "Químico/a Farmacéutico/a",
        "duracion": "5 años",
        "descripcion": "El Químico Farmacéutico es el profesional de la salud con sólida formación científico-humanista-cristiana y tecnológica que le permite liderar, innovar, "
            "emprender y comprometerse socialmente en el mantenimiento de la salud y de la calidad de vida de la población. Es experto en medicamentos, cosméticos, productos afines "
            "y otras sustancias químicas relacionadas. Está capacitado para realizar responsablemente el diseño, evaluación, desarrollo, producción, control, distribución, gestión "
            "de calidad y promoción del uso racional del medicamento.",
        "img": "/static/img/avatar-carreras/quimicaFarmacia-avatar.png"
    },
    {
        "carrera": "Psicología",
        "titulo": "Lic. en Psicología Clínica",
        "duracion": "5 años",
        "descripcion": "El psicólogo es un profesional que tiene las competencias para diagnosticar e intervenir en el área del ejercicio de la Psicología, con las técnicas y los instrumentos "
            "proporcionados por la Ciencia Psicológica. El profesional podrá desempeñarse en el área clínica como educacional.",
        "img": "/static/img/avatar-carreras/psicologia-avatar.png"
    },
    {
        "carrera": "Ingeniería Informática",
        "titulo": "Ingeniero Informático",
        "duracion": "5 años",
        "descripcion": "El Ingeniero Informático es un profesional capacitado para el manejo de los recursos informáticos. Instrumenta, analiza y diseña sistemas de información que permitirán el "
            "desarrollo integral de las organizaciones. Además, puede realizar tareas como estudio de factibilidad técnico económico para el desarrollo de software y redes, montaje y mantenimiento de "
            "sistemas informáticos. Asimismo, puede desempeñarse en empresas de desarrollo de software, área de las telecomunicaciones, instituciones públicas y privadas, financieras, industrias y empresas.",
        "img": "/static/img/avatar-carreras/ingenieriaInformatica-avatar.png"
    },
    {
        "carrera": "Ingeniería Química",
        "titulo": "Ingeniero Químico",
        "duracion": "5 años",
        "descripcion": "El Ingeniero Químico es un profesional que conoce los fundamentos de las ciencias básicas y las ciencias naturales, de las operaciones unitarias y de los procesos químicos, "
            "con la finalidad de efectuar la transformación de la materia prima y energía en productos terminados, empleando “tecnologías limpias” y cuidando la economía de los procesos. Además, "
            "puede realizar tareas como la construcción, montaje de equipos y plantas, control de producción y control ambiental. Asimismo, puede desempeñarse en sectores de industrias químicas y petroquímicas, "
            "alimentos y bebidas, biotecnología, generación de energía y farmacéutica.",
        "img": "/static/img/avatar-carreras/ingenieriaQuimica-avatar.png"
    },
    {
        "carrera": "Ingeniería Industria",
        "titulo": "Ingeniero Industrial",
        "duracion": "5 años",
        "descripcion": "Los/as ingenieros/as industriales son profesionales que permiten el desarrollo sustentable de la industria, contemplando la variable ambiental en el proceso. "
            "Su trabajo permitirá la optimización de los recursos disponibles, minimizando su impacto a través del uso apropiado de la tecnología, cuidando el aspecto social de los proyectos. "
            "Además, pueden desempeñarse en el diseño de proyectos en empresas industriales y de servicios, gerenciamiento en empresas industriales, auditorías de calidad, gestión de políticas, "
            "control y fiscalización en el ámbito de las industrias.",
        "img": "/static/img/avatar-carreras/ingenieriaIndustrial-avatar.png"
    }
]

# Preguntas
questions = {
    "Apertura a la experiencia" : [
        "¿Te gustan las actividades creativas como escribir o pintar?",
        "¿Te sientes a gusto al conversar con personas que tienen ideas y experiencias diferentes a las tuyas?",
        "¿Te gusta explorar nuevas ideas y conceptos?",
        "¿Eres adaptable a nuevas situaciones y cambios en tu vida?",
        "¿Te gusta experimentar con nuevas tecnologías y aplicaciones?",
        "¿Eres curioso/a acerca de cómo funcionan las cosas en el mundo?"
    ],
    "Conciencia" : [
        "¿Te consideras una persona organizada en tus actividades diarias?",
        "¿Te molesta cuando las cosas no se hacen bien y a tiempo?",
        "¿Eres exigente con tus actividades?",
        "¿Te esfuerzas por seguir reglas y normas establecidas?",
        "¿Prefieres completar tus tareas antes de disfrutar de un descanso?",
        "¿Te consideras una persona en la que los demás pueden confiar?"
    ],
    "Extraversión" : [
        "¿Te desenvuelves fácilmente en situaciones sociales?",
        "¿Participas en actividades grupales o trabajas en equipo?",
        "¿Sientes incomodidad al interactuar con personas que acabas de conocer?",
        "¿Te gusta ser el centro de atención en situaciones sociales?",
        "¿Los demás te consideran por ser extrovertido/a y comunicativo/a en diferentes contextos?",
        "¿Disfrutas asistir a eventos sociales como fiestas o reuniones?"
    ],
    "Amabilidad" : [
        "¿Dedicas tu tiempo para ayudar a los demás?",
        "¿Eres capaz de entender los sentimientos de otras personas?",
        "¿Evitas involucrarte en conflictos y prefieres la armonía?",
        "¿Te esfuerzas por ser amable y cortés con los demás?",
        "¿Te gusta realizar actos de bondad sin esperar recompensa?",
        "¿Te preocupas por el bienestar de los demás?"
    ],
    "Neuroticismo" : [
        "¿Sientes emociones negativas en demasía como preocupación o ansiedad?", 
        "¿Te resulta difícil controlar tus emociones?",
        "¿Te irritas fácilmente ante los cambios inesperados?",
        "¿Tienes preocupación en exceso por situaciones pequeñas?",
        "¿Te afectan mucho las críticas o comentarios negativos?",
        "¿Te consideras alguien que necesita apoyo emocional en momentos difíciles?"
    ]
}

# detalle de los rasgos
traitDetails = {
    "Apertura a la experiencia": {
        (0, 20): "Las personas cerradas a las experiencias prefieren lo convencional y seguro. Prefieren actividades técnicas y concretas, mostrando poco interés en lo abstracto. Son prácticas, directas, organizadas y centradas",
        (21, 40): "Las personas moderadamente cerradas a las experiencias prefieren lo convencional y seguro, optando por actividades técnicas y concretas y mostrando menos interés en lo abstracto",
        (41, 60): "Las personas moderadamente cerradas y abiertas a las experiencias mantienen una rutina organizada, pero no de manera estricta. Son prácticas y abiertas a nuevas ideas, aprecian los conceptos abstractos y el arte, y también realizan actividades técnicas y concretas",
        (61, 80): "Las personas moderadamente abiertas a las experiencias son imaginativas y curiosas. No se apegan a rutinas estrictas y disfrutan de diversas formas de arte, cultura y expresión",
        (81, 100): "Las personas altamente abiertas a experiencias son imaginativas, creativas, y aventureras. No se apegan a rutinas estrictas y disfrutan de diversas formas de arte y cultura. Son hábiles para encontrar soluciones inusuales y conexiones inesperadas"
    },
    "Conciencia": {
        (0, 20): "Las personas con bajo autocontrol son arriesgadas y viven el momento, pero pueden ser impulsivas, distraídas y poco perseverantes en la consecución de metas futuras. Priorizan satisfacer necesidades inmediatas sin considerar el impacto en sus planes a largo plazo",
        (21, 40): "Las personas con moderado autocontrol son arriesgadas pero pueden ser impulsivas, distraídas y poco perseverantes en la ejecución de sus planes o metas futuras",
        (41, 60): "Las personas con moderado autocontrol son flexibles y disfrutan del ocio, aunque siguen planes para alcanzar metas. Son perseverantes y organizadas, sin ser perfeccionistas o controladoras",
        (61, 80): "Las personas con moderado autocontrol son organizadas y meticulosas, pero pueden ser impulsivas y distraídas. Son disciplinadas, perseverantes y tienden a cumplir metas",
        (81, 100): "Las personas con gran autocontrol son organizadas y puntuales, percibidas como confiables. Tienen facilidad para postergar gratificaciones y cumplen metas a largo plazo, pero pueden caer en perfeccionismo y adicción al trabajo"
    },
    "Extraversión": {
        (0, 20): "Las personas introvertidas se recargan solas o en grupos pequeños. Les gusta trabajar solas, son reservadas y desconfian de las personas desconocidos, además se sienten incómodas en grupos grandes",
        (21, 40): "Las personas moderadamente introvertidas se recargan solas o en grupos pequeños. Son reservadas, pensativas y prefieren trabajar individualmente",
        (41, 60): "Las personas moderadamente introvertidas y extrovertidas son reservadas al socializar con desconocidos pero pueden ser expresivas con personas de confianza",
        (61, 80): "Las personas moderadamente extrovertidas se recargan pasando el tiempo con otras personas y en lugares frecuentes. Trabajan bien en grupo y son optimistas y entusiastas",
        (81, 100): "Las personas extrovertidas se recargan pasando el tiempo con otras personas y en lugares frecuentes. Son expresivas, sociables, buscan atención y reconocimiento social. Trabajan bien en grupo, además son optimistas y entusiastas"
    },
    "Amabilidad": {
        (0, 20): "Las personas con baja amabilidad son competitivas y enfocadas en sus metas, lo que puede hacerlas parecer egocéntricas y frías. Suelen experimentar menos empatía y priorizan sus propias necesidades sobre las de los demás",
        (21, 40): "Las personas con baja amabilidad son competitivas y enfocadas en sus metas, lo que puede dar la impresión de ser egocéntricas y frías",
        (41, 60): "Las personas moderadamente amables son colaboradoras y atentas, sin descuidar sus propios intereses. Cooperan y aportan al equipo sin perder su competitividad personal",
        (61, 80): "Las personas moderadamente amables son empáticas y solidarias, disfrutan servir y cuidar a los demás",
        (81, 100): "Las personas amables son empáticas y solidarias, disfrutan servir y cuidar a los demás. Son comprensivas y tolerantes, incluso con personas hostiles, pero pueden ser demasiado confiadas y poner las necesidades de los demás por encima de las suyas"
    },
    "Neuroticismo": {
        (0, 20): "Las personas con alta estabilidad emocional son tranquilas y manejan bajo estrés, aunque pueden ser demasiado apacibles en situaciones extremas",
        (21, 40): "Las personas emocionalmente estables son tranquilas, seguras y positivas, aunque pueden ser demasiado apacibles en situaciones extremadamente tensas",
        (41, 60): "Las personas con niveles moderados de estabilidad emocional pueden reaccionar según la situación y responden rápidamente ante el peligro, pero también son prudentes, calmadas y seguras",
        (61, 80): "Las personas con baja estabilidad emocional reaccionan ante el peligro, pero pueden tener un comportamiento impredecible y tienden a sentirse ansiosas e inseguras",
        (81, 100): "Las personas con baja estabilidad emocional reaccionan en situaciones amenazantes, pero su comportamiento es impredecible y sus reacciones varían ampliamente. Suelen sentirse constantemente ansiosas, culpables e inseguras"
    },

}

# Create your views here.

def home(request):
    if request.method == "POST" and "btnStartNow" in request.POST:
        request.session['final_questionary'] = False
        return redirect('registration')
    else:
        return render(request, 'home.html')

def registration(request):
    request.session['end_questionary'] = False
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            avatar = form.cleaned_data['avatar']
            userName = form.cleaned_data['userName']
            if avatar and userName:
                request.session['avatar'] = avatar
                request.session['userName'] = userName
                return redirect('/test/')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form' : form})

def test(request):
    if request.method == "GET":
        if 'avatar' in request.session and 'userName' in request.session:
            avatar = request.session['avatar']
            userName = request.session['userName']
            request.session['userNameFinal'] = userName
            request.session['values_list'] = []
            request.session['end_questionary'] = False
            request.session['trait_sums'] = {"Apertura a la experiencia": 0, "Conciencia": 0, "Extraversión": 0, "Amabilidad": 0, "Neuroticismo": 0}
            # del request.session['traitSums']

            del request.session['avatar']
            del request.session['userName']
            
            return render(request, 'questionary.html', {'avatar': avatar, 'userName': userName})
        else:
            return redirect('registration')    
    else:
        return redirect('registration')

def getQuestions(request):
    # Aplana el diccionario a una lista de tuplas
    flat_questions = [(trait, question) for trait, questions in questions.items() for question in questions]
    random.shuffle(flat_questions)
    
    return JsonResponse({'questions': flat_questions})

@csrf_exempt
def questionsResults(request):
    if request.method == 'POST':
        value = int(request.POST.get('value'))
        trait = request.POST.get('trait')
        endQuestionary = request.POST.get('endQuestionary')
        print("Value = ", value)
        print("Trait = ", trait)
        print("Final del cuestionario: ", endQuestionary)

        trait_sums = request.session.get('trait_sums', {"Apertura a la experiencia": 0, "Conciencia": 0, "Extraversión": 0, "Amabilidad": 0, "Neuroticismo": 0})
        trait_sums[trait] += value
        request.session['trait_sums'] = trait_sums
        print("Trait sums = ", trait_sums)

        values_list = list(trait_sums.values())
        request.session['values_list'] = values_list
        request.session['end_questionary'] = endQuestionary
        print("Values list = ", values_list)

        
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

def careerSelection(userResults, careers):
    # Convertir los porcentajes a enteros
    userResults = {k: int(v[:-1]) for k, v in userResults.items()}
    print("Resultados: ", userResults)

    # Crear un diccionario para almacenar las puntuaciones de las carreras
    career_scores = {career: 0 for career in careers}

    # Para cada carrera, sumar el porcentaje del usuario para cada rasgo relacionado
    for career, traits in careers.items():
        for trait in traits:
            if userResults[trait] > 70:  # Considerar solo los rasgos con un porcentaje mayor al 70%
                career_scores[career] += userResults[trait]

    # Ordenar las carreras por puntuación y devolver la lista
    sorted_careers = sorted(career_scores.items(), key=lambda item: item[1], reverse=True)
    return [career for career, score in sorted_careers if score == sorted_careers[0][1]]





def convertirPorcentaje(diccionario, maximo):
    for clave in diccionario:
        porcentaje = (diccionario[clave] / maximo) * 100
        diccionario[clave] = f'{porcentaje:.0f}%'
    return diccionario

def finalResults(request):
    trait_sums = request.session.get('trait_sums', [])
    endQuestionary = request.session.get('end_questionary')
    defaultTrait = ["Apertura a la experiencia", "Conciencia", "Extraversión", "Amabilidad", "Neuroticismo"]
    print("HOLAAA ", endQuestionary)
    if all(trait_sums[key] != 0 for key in defaultTrait) and endQuestionary is not False:
        # Si endQuestionary no es False, proceder con el procesamiento normal
        
        print("Suma de los puntajes por rasgo en porcentaje: ", trait_sums)

        personalidadPorcentaje = convertirPorcentaje(trait_sums, 30)
        print(personalidadPorcentaje)

        print("Resultados finales: ", careerSelection(personalidadPorcentaje, careers))
        careerSuggestion = careerSelection(personalidadPorcentaje, careers)
        userName = request.session['userNameFinal']
        userResults = {k: v[:-1] for k, v in personalidadPorcentaje.items()}
        colors = ['rgb(0, 187, 255)', 'rgb(136, 200, 25)', 'rgb(249, 228, 0)', 'rgb(221, 114, 0)', 'rgb(255, 0, 0)']
        print(userName)
        rasgosData = list(zip(userResults.items(), colors))
        detallesRasgos = generateTraitDetails(userResults)
        html_content = ""
        
        for (item, color), detalle in zip(rasgosData, detallesRasgos):
            progress_bar = f'<h5 class="custom-title" style="text-align:left;">{item[0]}</h5>' \
                        f'<div class="progress" role="progressbar" aria-valuenow="{item[0]}" aria-valuemin="0" aria-valuemax="100" style="height: 25px; box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.2);">' \
                        f'  <div class="my-progress-bar" style="width: {item[1]}%; background-color: {color}; text-align: center; line-height: 25px; font-weight: bold; color: black;">' \
                        f'   {item[1]}%' \
                        f'  </div>' \
                        f'</div>' \
                        f'<p>{detalle}</p>' \
                        f'<br>'
            html_content += progress_bar

        # Crear el contexto de la plantilla
        context = {
            'userName': userName,
            'html_content': html_content   # Agregar html_content al contexto
        }

        request.session['careerSuggestion'] = careerSuggestion

        return render(request, 'results.html', context)
    else:
        return redirect('registration')

def generateTraitDetails(userResults):
    detail = []
    for rasgo, valor in userResults.items():
        # Verifica si el rasgo tiene definidos mensajes en el diccionario
        if rasgo in traitDetails:
            # Encuentra el mensaje correspondiente al valor en el diccionario de mensajes para ese rasgo
            for rango, mensaje in traitDetails[rasgo].items():
                if rango[0] <= int(valor) <= rango[1]:
                    detail.append(mensaje)
                    break
    # Devuelve el array de detalles por cada rasgo
    return detail

def careerDetails(request):
    careerSuggestion = request.session.get('careerSuggestion', [])
    career_details = []
    print(careerSuggestion)

    for careerItem in careerSuggestion:
        for information in careersInformation:
            if information["carrera"] == careerItem:
                career_details.append({
                    "carrera": careerItem,
                    "titulo": information["titulo"],
                    "duracion": information["duracion"],
                    "descripcion": information["descripcion"],
                    "avatar": information["img"]
                })

    return render(request, 'detalles-de-carreras.html', {'career_details': career_details})

def aboutCalculationFunction(request):

    return render(request, 'funcion-de-calculo.html')