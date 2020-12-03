from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "A4/index.html")

def food(request):
    return render(request, "A4/food.html")

def name(request):
    return render(request, "A4/name.html")

def vacation(request):
    return render(request, "A4/vacation.html")

