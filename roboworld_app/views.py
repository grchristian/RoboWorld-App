from django.shortcuts import render

'''
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads
from . models import Reto
import psycopg2
'''

def inicio(request):
    return render(request, "roboworld_app/index.html")

def stats(request):
    return render(request, "roboworld_app/stats.html")

def micuenta(request):
    nombre = "Chritian"
    return render(request, "roboworld_app/micuenta.html", {"nombre":nombre}) 

def juego_unity(request):
    return render(request, "roboworld_app/juego_unity/index_unity.html")


def login(request):
    return render(request, "roboworld_app/login.html")

def logged_out(request):
    return render(request, "roboworld_app/logged_out.html")


def score(request):
    return render(request, "roboworld_app/score.html")

