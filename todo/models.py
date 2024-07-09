from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    text = models.CharField(max_length=255)
    is_checked = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
