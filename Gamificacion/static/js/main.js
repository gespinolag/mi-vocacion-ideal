$(document).ready(function() {
    // variables
    var points;
    var questions
    var currentQuestionIndex = -1;
    var totalQuestions;
    var likertInputs = document.querySelectorAll('input[name="likert"]');
    var nextButton = document.getElementById('nextBtn');
    var selectedLikertBtnValue;


    // Solicitud AJAX para cargar preguntas
    $.ajax({
        url: "/obtener-preguntas/",
        type: "GET",
        success: function(data) {
            questions = data.questions;
            totalQuestions = questions.length;
            showNextQuestion();
        }
    })

    function showLoader() {
        $("#loaderSection").fadeIn(400, function() {
            document.getElementById('loader').style.display = 'block';
        }); 
    }
    
    function hideLoader() {
        document.getElementById('loader').style.display = 'none';
    }

    function showNextQuestion() {
        currentQuestionIndex++;
        if(currentQuestionIndex < questions.length) {
            $("#question").fadeOut(400, function() {
                $(this).text(questions[currentQuestionIndex]).fadeIn(400);
            });
            document.querySelectorAll('input[name="likert"]').forEach((radio) => {
                radio.checked = false;
                checkLikertSelection();
            });
        } else {
            console.log("CurrentQuestionIndex: " + currentQuestionIndex);
            showLoader();
            document.getElementById("nextBtn").disabled = true;
            document.querySelectorAll('input[name="likert"]').forEach((radio) => {
                radio.disabled = true;
            });

            setTimeout(function(){  
                document.getElementById('loader').style.display = 'none';
                window.location.href = "/results/";
            }, 3000);
        }
    }

    document.getElementById("nextBtn").addEventListener("click", function() {
        showNextQuestion();
        var progress = ((currentQuestionIndex) / totalQuestions) * 100;
        $(".progress-bar").css("width", progress + "%").attr("aria-valuenow", progress);
    });


    function checkLikertSelection() { //verifica si algun boton de las opciones se presiono para habilitar bt "Siguiente"
        var anyChecked = false;
        for (var i = 0; i < likertInputs.length; i++) {
            if (likertInputs[i].checked) {
                anyChecked = true;
                break;
            }
        }
        nextButton.disabled = !anyChecked;
    }

    likertInputs.forEach(function(input) {
        input.addEventListener('change', checkLikertSelection);
    });


    $('input[name="likert"]').on('change', function() {
        selectedLikertBtnValue = $(this).val();
    });

    $('#nextBtn').on('click', function() {
        if(selectedLikertBtnValue !== null){
            $.ajax({
                url: '/enviar-resultados/',
                type: 'POST',
                data: {
                    value: selectedLikertBtnValue,
                    index: currentQuestionIndex
                }
            });
        }
    });
});