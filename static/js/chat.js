var socket = io();


socket.on('connect', function() {
    socket.emit('join_chat', {data: 'I\'m connected!'});
});

socket.on('my_response', function(msg, cb) {
    var log = document.getElementById("log");
    var br = document.createElement("br");
    var newDiv = document.createElement("div");
    var newContent = document.createTextNode(msg.data);
    newDiv.appendChild(newContent); //añade texto al div creado.

    // añade el elemento creado y su contenido al DOM
    var currentDiv = document.getElementById("chat");
    document.body.insertBefore(br, currentDiv);
    document.body.insertBefore(newDiv, currentDiv);
    
    if (cb)
        cb();
});


function iniciarSession(){
    var nombre = document.getElementById("user");
    socket.emit('iniciarSession', {nombre: nombre.value});
    return false;
}

function enviarMensaje(){
    var message = document.getElementById("message");
    socket.emit('mensaje', {message: message.value});
    return false;


}