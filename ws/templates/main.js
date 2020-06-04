$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/ws');
    socket.on('processed', function(msg) {
        alert('Received: ' + msg.data);
    });
    $('form').submit(function(event) {
        console.log('hey');
        socket.emit('add_to_queue', {data: $('#data').val()});
        return false;
    });
});
