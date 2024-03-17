from django.core.exceptions import ValidationError
from django.db import models
from django_telegram_bot.models import TelegramModel
from django.utils import timezone
from datetime import datetime
from .models import Task
import re

class Bot_data(TelegramModel):
    name = models.CharField(max_length=100)
    text = models.TextField()
    data_time = models.DateTimeField(default=timezone.now)
    
    "Функция для конвертации объекта datetime в UNIX"
    def save(self, *args, **kwargs):
        if not self.id:
            self.date_timestamp = int(self.date.strftime('%s'))
        super().save(*args, kwargs)

    "Функия для валидации времени"
    def clean_date(value):
        if not re.match(r'\d{8}', value):
            raise ValidationError({'date': 'Invalid date formate.'})
        return value

    def __str__(self):
        return self.name

    
   
    
