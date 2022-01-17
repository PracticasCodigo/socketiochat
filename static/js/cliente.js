var socket = io();

socket.on('id_Cliente', function() {
});

socket.emit('id_Cliente');


socket.on('my_response', function(msg, cb) {
    var br = document.createElement("br");
    var newDiv = document.createElement("div");
    var newContent = document.createTextNode(msg.data);
    newDiv.appendChild(newContent); //añade texto al div creado.

    // añade el elemento creado y su contenido al DOM
    var currentDiv = document.getElementById("log");
    document.body.insertBefore(br, currentDiv);
    document.body.insertBefore(newDiv, currentDiv);
    
    if (cb)
        cb();
});
