var WS_API = 'ws://127.0.0.1:8080/ws';
var socket = null;

$(function() {
  socket = new WebSocket(WS_API);
  if (socket) {
    socket.onopen = function() {
        console.log('Connected to:', WS_API);
    }

    socket.onclose = function(e) {
        console.log('Connection closed:', JSON.stringify(e));
        socket = null;

        $("canvas").animate({
            left: '250px',
            opacity: '0.5',
            height: '150px',
            width: '150px'
        });

    }

    socket.onmessage = function(e) {
      console.log('msg:', e.data);
      payload = JSON.parse(e.data);
      console.log(payload.structures.mine["x-location"]);
      var xloc= payload.structures.mine["x-location"];


      var c=document.getElementById("mycanvas");
      var ctx=c.getContext("2d");
      ctx.rect(xloc,20,150,100);
      ctx.stroke();

    }
  }
});

$('#submit-message').click(function() {
  var msg = $('#message').val();
  if (socket) {
    socket.send(msg);
  }
});
