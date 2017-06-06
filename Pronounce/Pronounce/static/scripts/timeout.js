$('#splash').ready()
{
    $('#main').load('sentences.html');
    setTimeout(function () {
        $('#main').ready(function () {
            $('#splash').remove();
            window.location.href = "/sentences/0";
        });
    }, 20000);
}       