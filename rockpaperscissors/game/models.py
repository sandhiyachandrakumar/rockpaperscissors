from django.db import models

class GameResult(models.Model):
    user_choice = models.CharField(max_length=10)
    computer_choice = models.CharField(max_length=10)
    result = models.CharField(max_length=20)
    played_at = models.DateTimeField(auto_now_add=True)

