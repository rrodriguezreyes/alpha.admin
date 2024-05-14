from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    days_creation_below_operational_hour = models.IntegerField()
    days_creation_above_operational_hour = models.IntegerField()
    days_creation_below_operational_hour_reinvestment = models.IntegerField()
    days_creation_above_operational_hour_reinvestment = models.IntegerField()
    operational_hour = models.TimeField()
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'products'
