from django.db import models

# Create your models here.

class Faculty_Department(models.Model):
    IT=models.CharField(max_length=20)
    Mechanical=models.CharField(max_length=20)
    Electrical=models.CharField(max_length=20)
    Teachers=models.CharField(max_length=20)


    class Meta:
        db_table = "Faculty_Department"
