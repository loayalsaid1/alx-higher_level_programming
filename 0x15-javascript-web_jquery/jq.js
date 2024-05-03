$(document).ready( function () {
    $("#start").click( function () {
        $("p").toggleClass("red")
    });
    $("#stop").click(function () {
        $("h2").remove();
    })

    $("#x").text($("#content").outerwidth(true))
})
