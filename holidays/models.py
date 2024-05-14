from django.db import models

class Holiday(models.Model):
    id = models.AutoField(primary_key=True)
    holiday_date = models.DateField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'holidays'
