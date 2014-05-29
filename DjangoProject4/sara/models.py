from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=200,blank = True,null = True)
    email=models.CharField(max_length=200)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name