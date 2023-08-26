import uuid

from django.db import models

class Letter(models.Model):
    displayed_name = models.CharField(max_length=120)
    message = models.TextField(max_length=1000)
    reviewed = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f'{self.displayed_name} | {self.message[:50]}'


