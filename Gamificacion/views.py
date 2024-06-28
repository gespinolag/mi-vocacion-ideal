from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
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
questionList = {
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
    request.session['last_question'] = False
    if 'trait_sums' in request.session:
        del request.session['trait_sums']
    if request.method == "POST" and "btnStartNow" in request.POST:
        return redirect('registration')
    else:
        request.session.flush()
        return render(request, 'home.html')

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            avatar = form.cleaned_data['avatar']
            userName = form.cleaned_data['userName']
            if avatar and userName:
                request.session['avatar'] = avatar
                request.session['userName'] = userName
                return redirect('/cuestionario/')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form' : form})

def questionary(request):
    if request.method == "GET":
        if 'avatar' in request.session and 'userName' in request.session:
            avatar = request.session.get('avatar', '')
            userName = request.session['userName']
            request.session['userNameFinal'] = userName
            request.session['userAvatarFinal'] = avatar

            if 'trait_sums' in request.session:
                del request.session['trait_sums']
            if avatar == 'bob':
                avatarFinal = '/static/img/bob-avatar-pq.png'
            else:
                avatarFinal = '/static/img/alice-avatar-pq.png'

            del request.session['avatar']
            del request.session['userName']
            
            return render(request, 'questionary.html', {'avatar': avatarFinal, 'userName': userName})
        else:
            return redirect('registration')    
    else:
        return redirect('registration')

def questions(request):
    # Aplana el diccionario a una lista de tuplas
    flat_questions = [(trait, question) for trait, questions in questionList.items() for question in questions]
    random.shuffle(flat_questions)
    
    return JsonResponse({'questions': flat_questions})

@csrf_exempt
def sendResults(request):
    lastQuestion = False
    if request.method == 'POST':
        value = int(request.POST.get('value')) # obtenemos el valor de la escala de Likert
        trait = request.POST.get('trait') # obtenemos el rasgo de acuerdo al valor
        endQuestionary = request.POST.get('endQuestionary') # valor para saber si el cuestionario finalizó
        request.session['end_questionary'] = endQuestionary # se guarda en sesión valor para saber si el cuestionario finalizó

        # Mapeo de los rasgos a las posiciones del array
        trait_map = {
            "Apertura a la experiencia": 0,
            "Conciencia": 1,
            "Extraversión": 2,
            "Amabilidad": 3,
            "Neuroticismo": 4
        }
        
        # Obtener la lista de la sesión o inicializarla si no existe
        trait_sums = request.session.get('trait_sums', [0, 0, 0, 0, 0])

        # Actualizar el valor correspondiente al rasgo
        if trait in trait_map:
            index = trait_map[trait]
            trait_sums[index] += value

        # Guardar la lista actualizada en la sesión
        request.session['trait_sums'] = trait_sums
        print("Trait sums =", trait_sums)
        
        if endQuestionary == 'true':
            lastQuestion = True
            request.session['last_question'] = lastQuestion
            # Redirigir a la vista finalResults
            return HttpResponseRedirect(reverse('resultados'))      # Ajusta según tus URLs y nombres de vista
        else:
            lastQuestion = False
            request.session['last_question'] = lastQuestion
            # Devolver una respuesta de éxito
            return JsonResponse({'message': 'Valor recibido'}, status=200)

    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def finalResults(request):
    if request.session.get('results_processed', False): # verificamos si los resultados ya fueron procesados
        # si ya se procesaron los resultados del usuario obtenemos los datos de la sesión y renderizamos la plantilla de resultados (results.html)
        careerSuggestion = request.session.get('career_suggestion', [])
        userName = request.session.get('userNameFinal', '')
        avatar = request.session.get('userAvatarFinal', '')
        userCareerDetails = showCareerDetails(careerSuggestion)
        if avatar == 'bob':
            userAvatar = '/static/img/bob-avatar-pq.png'
        else:
            userAvatar = '/static/img/alice-avatar-pq.png'
        context = {
            'userName': userName,
            'careerDetails': userCareerDetails,
            'userAvatar': userAvatar
        }
        return render(request, 'results.html', context)
        # response = render(request, 'results.html', context)
        # request.session.flush()
        # return response
    
    trait_sums = request.session.get('trait_sums', []) # obtenemos los valores obtenidos por el usuario para cada rasgo en base a la escala de Likert
    last_question = request.session.get('last_question') # variable para saber si el usuario respondió a la última pregunta
    rasgos = ["Apertura a la experiencia", "Conciencia", "Extraversión", "Amabilidad", "Neuroticismo"] # rasgos de personalidad
    userName = request.session.get('userNameFinal', '') # obtenemos el nombre de usuario
    avatar = request.session.get('userAvatarFinal', '')
    # Imprimir información de depuración
    print(request.session.keys())
    print("Valor de trait_sums: ", trait_sums)
    print("Valor de last_question: ", last_question)
    if last_question is True:
        print("Valor de last_question dentro del if: ", last_question)
        totalQuestions = int(sum(len(preguntas) for preguntas in questionList.values())) # obtenemos el total de preguntas almacenadas en el array de preguntas
        personalidadPorcentaje = dict(zip(rasgos, convertirPorcentaje(trait_sums, totalQuestions))) # construimos el formato de los resultados del usuario con sus rasgos
        request.session['personalidad_porcentaje'] = personalidadPorcentaje # guardamos en sesión los valores de personalidad en porcentaje del usuario
        print("personalidadPorcentaje: ", personalidadPorcentaje)
        careerSuggestion = careerSelection(personalidadPorcentaje, careers) # llamada a función que devuelve las carreras en base a los resultados del usuario
        userCareerDetails = showCareerDetails(careerSuggestion) # llamada a función que devuelve dettales de las carreras en base a los resultados del usuario
        print("Carreras: ", careerSuggestion)
        request.session['results_processed'] = True # marcar que los resultados ya se procesaron
        request.session['career_suggestion'] = careerSuggestion # devuelve las carreras para vista de detalles de carreras
        print("Avatar: ", avatar)
        if avatar == 'bob':
            userAvatar = '/static/img/bob-avatar-pq.png'
        else:
            userAvatar = '/static/img/alice-avatar-pq.png'
        print("userAvatar: ", userAvatar)
        context = {
            'userName': userName,
            'careerDetails': userCareerDetails,
            'userAvatar': userAvatar
        }
        return render(request, 'results.html', context)
        # response = render(request, 'results.html', context)
        # request.session.flush()
        # return response
    else:
        print("Valor de last_question despues del if: ", last_question)
        return redirect('home')

def userTraitDetails(request):
    careerSuggestion = request.session.get('career_suggestion', [])
    userName = request.session.get('userNameFinal', '') # obtenemos el nombre de usuario
    personalidadPorcentaje = request.session.get('personalidad_porcentaje') # obtenemos los valores y rasgos del usuario
    colors = ['rgb(0, 187, 255)', 'rgb(136, 200, 25)', 'rgb(249, 228, 0)', 'rgb(221, 114, 0)', 'rgb(255, 0, 0)'] # colores de los rasgos
    rasgosData = list(zip(personalidadPorcentaje.items(), colors)) # se aocian los colores con los rasgos
    detallesRasgos = generateTraitDetails(personalidadPorcentaje) # llamada a la función para establecer la descripción de los rasgos segun porcentaje del usuario por rasgo
    html_content = ""
    for (item, color), detalle in zip(rasgosData, detallesRasgos):
            progress_bar = f'<h6 class="custom-title" style="text-align:left;">{item[0]}</h6>' \
                        f'<div class="progress" role="progressbar" aria-valuenow="{item[0]}" aria-valuemin="0" aria-valuemax="100" style="height: 25px; box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.2);">' \
                        f'  <div class="my-progress-bar" style="width: {item[1]}%; background-color: {color}; text-align: center; line-height: 25px; font-weight: bold; color: black;">' \
                        f'   {item[1]}%' \
                        f'  </div>' \
                        f'</div>' \
                        f'<p>{detalle}</p>' \
                        f'<br>'
            html_content += progress_bar

    suggestedCareers = {career: careers[career] for career in careerSuggestion if career in careers}
    # contexto de la plantilla
    context = {
        'userName': userName,
        'html_content': html_content, # html_content representan las barras de carga de los detalles de raagos
        'suggestedCareers': suggestedCareers # devolvemos a la plantilla las carreras con sus rasgos en base a los resultados del usuario
    }
    return render(request, 'detalles-de-rasgos.html', context)

# función para convertir en porcentaje los valores obtenidos del usuario
def convertirPorcentaje(traitSums, maximo):
    for i in range(len(traitSums)):
        porcentaje = (traitSums[i] / maximo) * 100
        traitSums[i] = int(porcentaje)
    return traitSums

# función de calculo de carreras en base a los puntos del usuario
def careerSelection(userResults, careers):

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


# función para devolver los datelles de los rasgos
def generateTraitDetails(userResults):
    detail = [] # Array de detalles por cada rasgo
    for rasgo, valor in userResults.items():
        # Verifica si el rasgo tiene definidos mensajes en el diccionario
        if rasgo in traitDetails:
            # Encuentra el mensaje correspondiente al valor en el diccionario de mensajes para ese rasgo
            for rango, mensaje in traitDetails[rasgo].items():
                if rango[0] <= int(valor) <= rango[1]:
                    detail.append(mensaje)
                    break
    return detail

# vista donde se muestran los detalles de las carreras
def careerDetails(request):
    careerSuggestion = request.session.get('career_suggestion', [])
    career_details = showCareerDetails(careerSuggestion)
    print(career_details)

    return render(request, 'detalles-de-carreras.html', {'career_details': career_details})

# función para mostrar detalles de las carreras
def showCareerDetails(careerSuggestion):
    career_details = []

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
    return career_details            

# vista pantalla función de cálculo
def aboutCalculationFunction(request):

    return render(request, 'funcion-de-calculo.html')