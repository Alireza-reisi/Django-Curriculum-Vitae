from django.db import models

# Create your models here.

class Experience(models.Model):
    title=models.CharField(max_length=50)
    timeline=models.CharField(max_length=40)
    description=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.title
    
    
class Education(models.Model):
    title=models.CharField(max_length=50)
    timeline=models.CharField(max_length=40)
    description=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.title
    
class Skill(models.Model):
    title=models.CharField(max_length=50)
    progress =models.IntegerField()   
    
    def __str__(self):
        return self.title