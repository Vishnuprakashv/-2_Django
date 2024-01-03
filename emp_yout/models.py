from django.db import models


# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    Phone_no=models.CharField( max_length=13)
    aadhar=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    dept=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    working=models.BooleanField(default=False)

    def __str__(self):
        return self.name
