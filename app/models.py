from django.db import models

class Table(models.Model):

    tid=models.CharField(max_length=100,primary_key=True)

class Webpage(models.Model):
    tid=models.ForeignKey(Table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()
class AccesssRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100,unique=True)
    date=models.DateField()


# Create your models here.
