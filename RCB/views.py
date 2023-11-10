from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat(request):
    return render(request,'virat.html')

def maxwell(request):
    return HttpResponse('''<center>
        <h1>Maxwell is the Best Batsman...</h1>
        <h1 style="color: coral;">Mr 360 </h1>
        <h1><marquee behavior="alternate" direction="left">He is the lefthand Batting man </marquee></h1></center>''')

def Rcb(request):
    return HttpResponse('<center><h1>Haii iam from ROYAL CHALLENGERS BANGALORE...!<h1 style="color:red">Welcome to <h1 style="color:Blue">INDIAN PREMIER LEAGUE')
