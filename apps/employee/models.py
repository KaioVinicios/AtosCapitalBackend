from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from apps.enterprise.models import Enterprise


class EmployeeUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  whatsapp_number = PhoneNumberField(region='BR', unique=True)
  enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='employee')
  
  # def save(self, *args, **kwargs):    
  #   if self.user:
  #     self.name = f"{self.user.first_name} {self.user.last_name}".strip()
  #   super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.name} - {self.whatsapp_number}"