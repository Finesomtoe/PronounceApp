function preventBack() { window.history.forward(); }
setTimeout("preventBack()", 0);
window.onunload = function () { null };

$(function () {
    setTimeout(function () {
        return $(".bar").animate({
            height: "toggle"
        }, "slow")
    }, 450);
    return $("#ok").on("click", function () {
        $("#barwrap").css("margin-bottom", "0px");
        $(".bar").animate({
            height: "toggle"
        }, "slow");
        return !1
    })
});