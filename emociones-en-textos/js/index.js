$(document).ready(function () {

    $("#buscar").on("click", () => {
        var texto = $("#textaAnalizar").val();
        $.ajax({
            url: 'http://localhost:3000/analizarTexto',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({ texto: texto }),
            success: function(data) {
                console.log(data);
                $("#inputRespuesta").val(data.Servicio);
                console.log(data.Servicio);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });

    });
});

