from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    return render(request,'Applogin/index.html')