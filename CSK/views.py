from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')

def raina(request):
    return HttpResponse('<center> <h1> Raina is the best lefthand batsman </h1></center>')

def Csk(request):
    return HttpResponse('<center><h1>Haii iam from CHENNAI SUPER KINGS...!<h1 style="color:yellow">Welcome to <h1 style="color:Blue">INDIAN PREMIER LEAGUE')

