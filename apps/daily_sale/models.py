from django.db import models
from apps.branche.models import Branche

class DailySale(models.Model): 
  date = models.DateField(auto_now=False, auto_now_add=False)
  value = models.DecimalField(max_digits=15, decimal_places=2)
  goal = models.DecimalField(max_digits=5, decimal_places=2)
  branche = models.ForeignKey(Branche, on_delete=models.CASCADE, related_name='daily_sale')

  def __str__(self):
    return f"{self.id}"