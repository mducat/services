$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':8000/');

    socket.on('processed', function(msg) {
        alert('Received: ' + msg.data);
    });
    $('form').submit(function(event) {
        socket.emit('add_to_queue', {data: $('#data').val()});
        return false;
    });
});
