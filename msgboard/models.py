from django.db import models
from django.utils import timezone


class Message(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    @classmethod
    def main_feed(cls):
        """Get the list of messages to display on
       the
        Main feed page
        return: A QuerySet containing all the
       messages
        ordered from the newest to the
       oldest
        """

        return cls.objects.order_by('-date')
