# chat/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer
from .views import respond_to_websockets
from .models import ButtonTracker


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        # print(self.user.id)
        # print(self.user.username)
        obj = ButtonTracker.objects.get_or_create(user=self.user)
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # message = text_data_json["text"]
        joke = respond_to_websockets(text_data_json, self.user)


        self.send(text_data=json.dumps({"text": joke["text"]}))