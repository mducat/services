$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':8000/ws');
    socket.on('processed', function(msg) {
        console.log('hey');
        alert('Received: ' + msg.data);
    });
    $('form').submit(function(event) {
        socket.emit('add_to_queue', {data: $('#data').val()});
        return false;
    });
});
