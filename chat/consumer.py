from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json


class ChatRoomConsumer(AsyncWebsocketConsumer):
    # pass
    async def connect(self):
        # Called on connection.
        # To accept the connection call:
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print(self.room_name)
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.room_group_name)
        await self.accept()
        #
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        #
        await self.send(text_data=json.dumps({
            "status": "conected"
        }))
    #
    #
    #     await self.close()
    #
    # async def receive(self, text_data=None, bytes_data=None):
    #     # Called with either text_data or bytes_data for each frame
    #     # You can call:
    #     await self.send(text_data="Hello world!")
    #     # Or, to send a binary frame:
    #     await self.send(bytes_data="Hello world!")
    #     # Want to force-close the connection? Call:
    #     await self.close()
    #     # Or add a custom WebSocket error code!
    #     await self.close(code=4123)
    #
    # async def disconnect(self, close_code):
    #     pass
    # Called when the socket closes
