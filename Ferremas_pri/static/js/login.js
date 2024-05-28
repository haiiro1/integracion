// static/js/login.js
$(document).ready(function() {
    $(".open-modal").click(function(e) {
        e.preventDefault();
        $("#ModalLogin").css("display", "block");
    });

    $(".close").click(function() {
        $("#ModalLogin").css("display", "none");
    });

    $(window).click(function(event) {
        if ($(event.target).is("#ModalLogin")) {
            $("#ModalLogin").css("display", "none");
        }
    });
});