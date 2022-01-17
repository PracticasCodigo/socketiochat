var socket = io();


function accion(accion){
    var sid = document.getElementById("sid");
    socket.emit('accion', {accion: accion, sid: sid.value});
    return false;
}
