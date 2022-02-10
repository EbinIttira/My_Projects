from django.shortcuts import render
from .models import Place
from .models import Team
def demo(request):
   obj=Place.objects.all()
   objs = Team.objects.all()
   return render(request,"index.html",{'result':obj,'team':objs})

def about(request):
   return render(request,"About.html")

def contact(request):
   return render(request,"contact.html")