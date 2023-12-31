from django.db import models
from django.contrib.auth import  get_user_model


User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username + " " + str(self.timestamp)

    @staticmethod
    def last_10_messages():
        return  Message.objects.order_by('timestamp').all()[:10]
