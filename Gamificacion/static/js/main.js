$(document).ready(function() {
    $("#btnHome").click(function() {
        var registrationUrl = $("#registration-url").data("url");
        window.location.href = registrationUrl;
    });
});
