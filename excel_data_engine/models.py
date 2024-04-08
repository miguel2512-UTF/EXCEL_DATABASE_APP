from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Excel(models.Model):
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    refresh = models.BooleanField(default=True)
    data = models.JSONField(default=dict)
    records_length = models.CharField(max_length=500)
    api_url = models.CharField(max_length=500, default="")
    api_isactive = models.BooleanField(default=False)
    api_password = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "excel_database"