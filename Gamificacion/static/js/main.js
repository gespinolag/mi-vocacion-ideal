$(document).ready(function() {
    // variables
    var points;
    var questions
    var currentQuestionIndex = -1;
    var totalQuestions;

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

    function showNextQuestion() {
        currentQuestionIndex++;
        if(currentQuestionIndex < questions.length) {
            $("#question").fadeOut(400, function() {
                $(this).text(questions[currentQuestionIndex]).fadeIn(400);
            });
            document.querySelectorAll('input[name="likert"]').forEach((radio) => {
                radio.checked = false;
            });
        } else {
            document.getElementById("nextBtn").disabled = true;
        }
    }

    document.getElementById("nextBtn").addEventListener("click", function() {
        showNextQuestion();
        var progress = ((currentQuestionIndex + 1) / totalQuestions) * 100;
        $(".progress-bar").css("width", progress + "%").attr("aria-valuenow", progress);
    });

});
