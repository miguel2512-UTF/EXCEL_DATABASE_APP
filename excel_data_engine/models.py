from django.db import models

# Create your models here.
class Excel(models.Model):
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    refresh = models.BooleanField(default=True)
    data = models.JSONField(default=dict)
    records_length = models.CharField(max_length=500)

    class Meta:
        db_table = "excel_database"