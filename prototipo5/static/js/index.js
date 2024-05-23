var comentarios = {}

$(document).ready(function () {

    $("#buscar").on("click", () => {
        var texto = $("#textaAnalizar").val();
        $.ajax({
            url: 'http://localhost:3000/analizarTexto',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({ texto: texto }),
            success: function (data) {
                console.log(data);
                $("#inputRespuesta").val(data.Servicio);
                console.log(data.Servicio);
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        });

    });

    $("#buscarComentario").on("click", () => {
        $.ajax({
            url: 'http://localhost:3000/comentarioAleatorio',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                console.log(data);
                $("#textaAnalizar").val(data.Comentario.comentario);
                console.log(data.Comentario.comentario);
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        });

    });

    $("#btnPositivo").on("click", () => {
        $.ajax({
            url: `http://localhost:3000/comentarios?tipoComentario=positivo`,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                $(".comentarios-resultado").empty();
                console.log(data)
                for (let i = 0; i < data.Comentario.length; i++) {
                    console.log(data.Comentario[i])
                    agregarComentarios(1, data.Comentario[i])
                }
                // comentarios = data;
                $("#cantidadComentarios").text(data.Comentario.length + " comentarios")
                btnBorrar.style.display = "block";
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        })
    });

    $("#btnNeutro").on("click", () => {
        $.ajax({
            url: `http://localhost:3000/comentarios?tipoComentario=neutral`,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                $(".comentarios-resultado").empty();
                console.log(data)
                for (let i = 0; i < data.Comentario.length; i++) {
                    console.log(data.Comentario[i])
                    agregarComentarios(2, data.Comentario[i])
                }
                $("#cantidadComentarios").text(data.Comentario.length + " comentarios")
                // comentarios = data;
                btnBorrar.style.display = "block";
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        })
    });


    $("#btnNegativo").on("click", () => {
        $.ajax({
            url: `http://localhost:3000/comentarios?tipoComentario=negativo`,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                $(".comentarios-resultado").empty();
                console.log(data)
                for (let i = 0; i < data.Comentario.length; i++) {
                    console.log(data.Comentario[i])
                    agregarComentarios(3, data.Comentario[i])
                }
                // comentarios = data;
                $("#cantidadComentarios").text(data.Comentario.length + " comentarios")
                btnBorrar.style.display = "block";
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        })
    });

    

    // $("#btnPositivo").on("click", () => {
    //     $.ajax({
    //         type: "GET",
    //         url: "http://localhost:3000/comentarios",
    //         // contentType: "jsonp",
    //         data: JSON.stringify(cuerpo),
    //         xhrFields: {
    //             onprogress: function(e) {
    //                 var response = e.currentTarget.response;
    //                 var lines = response.split('\n');
    //                 var textoAnterior = $("#textaRespuesta").text()
    //                 lines.forEach(function(line) {
    //                     if (line.trim() !== '') {
    //                         var responseObject = JSON.parse(line);
    //                         // Hacer algo con el objeto de respuesta, por ejemplo, imprimirlo
    //                         console.log(responseObject);
    //                         $("#textaRespuesta").text(`${textoAnterior}${responseObject.response}`);
    //                     }
    //                 });
    //             }
    //         },
    //     }).done(function(data){
    //         console.log(data)
    //     });
    // });
});

const titulos = {
    1: "Positivo",
    2: "Neutral",
    3: "Negativo"
};

function agregarComentarios(tipo, data) {
    console.log(data)
    var titulo = titulos[tipo];
    var card = `
    <div class="card">
        <div class="card-header">
            ${titulo}
        </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item">${data.usuario}</li>
            <li class="list-group-item">${data.comentario}</li>
        </ul>
    </div>`
    $(".comentarios-resultado").append(card);
}

function buscarComentarios(tipo) {
    $.ajax({
        url: `http://localhost:3000/comentarios?tipoComentario=${tipo}`,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            console.log(data)
            comentarios = data;

        },
        error: function (xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
    // $.ajax({
    //     type: "GET",
    //     url: `http://localhost:3000/comentarios?tipoComentario=${tipo}`,
    //     // contentType: "jsonp",
    //     xhrFields: {
    //         onprogress: function (e) {
    //             console.log(e.currentTarget.response);
    //             // var response = e.currentTarget.response;
    //             // var lines = response.split('\n');
    //             // var textoAnterior = $("#textaRespuesta").text()
    //             // lines.forEach(function (line) {
    //             //     if (line.trim() !== '') {
    //             //         var responseObject = JSON.parse(line);
    //             //         // Hacer algo con el objeto de respuesta, por ejemplo, imprimirlo
    //             //         console.log(responseObject);
    //             //         $("#textaRespuesta").text(`${textoAnterior}${responseObject.response}`);
    //             //     }
    //             // });
    //         }
    //     },
    // }).done(function (data) {
    //     console.log(data)
    // });
}

var btnBorrar = document.getElementById("btnBorrar");
btnBorrar.addEventListener("click", () => {
    $(".comentarios-resultado").empty();
    btnBorrar.style.display = "none";
    $("#cantidadComentarios").text("")
});

document.addEventListener('DOMContentLoaded', function () {
    const textarea = document.getElementById('textaAnalizar');

    textarea.addEventListener('input', function () {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });
});