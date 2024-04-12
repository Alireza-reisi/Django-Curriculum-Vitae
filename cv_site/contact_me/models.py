from django.db import models



class contact(models.Model):
    name = models.CharField(max_length=30)
    gmail = models.EmailField(max_length=254)
    text = models.TextField()

    
    def __str__(self):
        return self.name