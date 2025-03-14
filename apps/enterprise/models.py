from django.db import models


class Enterprise(models.Model):
  name = models.CharField(max_length=255, unique=True)
  email = models.EmailField(unique=True)
  url_name = models.CharField(max_length=20, unique=True, primary_key=True)
  cnpj = models.CharField(max_length=255, unique=True)

  def __str__(self):
    return f'{self.name}'