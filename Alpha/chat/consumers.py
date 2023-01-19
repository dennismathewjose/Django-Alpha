from channels.generic.websocket import AsyncWebSocketConusmer
import json

class chatConsumer(AsyncWebSocketConusmer):
    #join a room
    async def connect(self):
        self.room_group_name = 'Test-room'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        #leave a room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print('Disconnected ')

    async def receive(self, text_data):
        received_data = json.loads(text_data)
        message = received_data['message']

        await self.channel_layer.group_send(
            self.room_group_name,{
                'type' : 'send_message',
                'message' : message
            }
        )
    
    async def send_message(self, event):
        message = event['message']

        await self.send(text_data = json.dumps({
            'message' : message
        }))

