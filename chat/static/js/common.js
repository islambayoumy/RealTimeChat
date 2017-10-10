var socket = new WebSocket('ws://' + window.location.host);

socket.onopen = function open() {
    console.log('WebSockets connection created.');
};

socket.onmessage = function message(event) {
    $('#start').hide();

    var data = JSON.parse(event.data);
    var username = encodeURI(data['username']);
    var text = data['text'];

    $("#messages").append('<li><p><span class="user">'+ username +': </span><span class="msg">'
    + text +'</span></p></li>');
};

if (socket.readyState == WebSocket.OPEN) {
    socket.onopen();
}

// click listener for send button
$('#send').click(function(){
    var msg = $('#msg').val();
    socket.send(msg);
    $('#msg').val('');
});


// key press listener for "Enter"" key
$('#msg').keypress(function (e) {
    var key = e.which;
    if(key == 13){
        $('#send').click();
        return false;  
    }
}); 