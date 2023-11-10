from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(requset):
    return render(requset,'rohit.html')

def sky(request):
    return HttpResponse('<h1>Best batsman in the india </h1>')

def Mi(request):
    return HttpResponse('<center><h1>Haii iam from Mumbai INDIANS...!<h1 style="color:cyan">Welcome to <h1 style="color:Blue">INDIAN PREMIER LEAGUE')