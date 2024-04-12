from django.shortcuts import render
from .models import Experience,Education,Skill
def resume(request):
    experiences=Experience.objects.all().order_by("date").reverse()
    education=Education.objects.all().order_by("date").reverse()
    skills=Skill.objects.all().order_by("progress").reverse()
    return render(request,"resume.html",context={'experiences':experiences , 'educations':education, 'skills':skills })