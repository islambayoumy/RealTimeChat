from channels import Group
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http  
import json

# Connected to websocket.connect
@channel_session_user_from_http
def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("chat").add(message.reply_channel)

# Connected to websocket.receive
@channel_session_user
def ws_message(message):
    text = message.content.get('text')
    Group("chat").send({
        "text": json.dumps({
            "text": message["text"],
            "username": message.user.username,
        }),
    })

# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)

