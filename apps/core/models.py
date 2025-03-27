# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tbvendasdashboard(models.Model):
    idvendas = models.AutoField(db_column='idVendas', primary_key=True)  # Field name made lowercase.
    nrcnpj = models.CharField(db_column='nrCNPJ', max_length=14)  # Field name made lowercase.
    nmfilial = models.CharField(db_column='nmFilial', max_length=50)  # Field name made lowercase.
    dtvenda = models.CharField(db_column='dtVenda', max_length=10)  # Field name made lowercase.
    vlvenda = models.DecimalField(db_column='vlVenda', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    txmeta = models.DecimalField(db_column='txMeta', max_digits=4, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbVendasDashboard'
