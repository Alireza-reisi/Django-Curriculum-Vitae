from django.contrib import admin
from .models import Experience,Education,Skill
# Register your models here.

myModels = [Education, Experience, Skill] 
admin.site.register(myModels)