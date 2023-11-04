from django.shortcuts import render,HttpResponse

# Create your views here.
def home(r):
    return render(r,'home.html')

