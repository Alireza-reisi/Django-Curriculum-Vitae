from django.shortcuts import render
from .models import contact


def contact_me(request):
    if request.POST.get("nameContact"):
        contact.objects.create(name=request.POST.get("nameContact"), gmail= request.POST.get("emailContact"),text=request.POST.get("messageContact"))
    return render(request,"contact.html")

    

