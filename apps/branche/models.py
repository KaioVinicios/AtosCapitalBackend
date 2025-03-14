from django.db import models
from apps.enterprise.models import Enterprise

# Create your models here.
class Branche(models.Model):
  name = models.CharField(max_length=255)
  cnpj = models.CharField(max_length=255, unique=True)
  enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='branche')  

  def __str__(self):
    return f'{self.name}'