from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from json import loads, dumps
from . models import Reto
from random import randrange
import psycopg2


def grafica(request):
    #data = [ ['Age', 'Weight'], [ 8,      12], [ 4,      5.5], [ 11,     14],[ 4,      5],[ 3,      3.5],[ 6.5,    7]]
    data = [['Edad', 'Peso']]
    for i in range(0,11):
        x = randrange(100)
        y = randrange(100)
        data.append([x,y])
    datos_formato = dumps(data)    
    return render(request,'grafica.html', {'losDatos':datos_formato})

#envia a index (listo)
def inicio(request):
    return render(request, "roboworld_app/index.html")



#envia a estadistica 1º (listo)
def grafica1(request):
    return render(request, "roboworld_app/graficas/grafica1.html")


#envia al juego (listo)
def juego_unity(request):
    return render(request, "roboworld_app/juego_unity/index_unity.html")

#envia inciar sesión (listo)
def iniciar_sesion(request):
    return render(request, "roboworld_app/iniciar_sesion.html")

#envia a cuenta de usuario (pendiente, conectar con db)
@login_required
def cuenta_usuario(request):
    num_engranes = "43"
    min_jugados = "53"
    veces_jugadas = "5"
    return render(request, "roboworld_app/cuenta_usuario.html", {"num_engranes":num_engranes,"min_jugados":min_jugados,"veces_jugadas":veces_jugadas}) 


def proceso(request):
    nombre = request.POST['nombre']
    nombre=nombre.upper()
    
    return render(request, "proceso.html", {"nombre":nombre}) 

@login_required
def datos(request):
    jugadores = Reto.objects.all() #select * from Reto;
    return render(request, 'datos.html', {'lista_jugadores':jugadores})

@login_required
def score(request):
    usuario = request.user
    resultados = Reto.objects.filter(nombre=usuario)
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
    return render(request, 'score.html', {"nombreUsuario":nombre,"score":score})

@csrf_exempt
def unity(request):
    nombre = "Martin"
    score = "1234"
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)


'''
@csrf_exempt

def micuenta(request):
    session={
    num_engranes = "43"
    min_jugados = "53"
    veces_jugadas = "5"
    }
    return JsonResponse(session)
'''
@csrf_exempt

def buscaJugadorBody(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    resultados = Reto.objects.filter(nombre=jugador_nombre)  #select * from Reto where nombre = jugador_nombre
    
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
   
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)

@csrf_exempt
def ejemploSQL(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    nombre = ""
    score = ""

    try:
        connection = psycopg2.connect(
            user = "admin",
            password = "adminpass",
            host = "localhost",
            port = "5432",
            database = "dataroboworld"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roboworld_app_reto;")
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == jugador_nombre:
                nombre = row[1]
                score = row[2]
            print(row)
    
    except(Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL database', error)
        connection = None
    
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)

'''
Level
'''
@csrf_exempt
def Level(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    level_number = body_json['level_number']
    level_number = ""
    enemigo = ""
    dificultad = ""
    duracion_individual=""

    try:
        connection = psycopg2.connect(
            user = "admin",
            password = "adminpass",
            host = "localhost",
            port = "5432",
            database = "dataroboworld"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roboworld_app_level;")
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == level_number:
                level_number = row[1]
                enemigo = row[2]
                dificultad = row[3]
                duracion_individual=row[4]
            print(row)
    
    except(Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL database', error)
        connection = None
    
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
    retorno = {"level_number":level_number,
         "enemigo":enemigo,
         "dificultad":dificultad,
         "duracion_individual": duracion_individual}
    return JsonResponse(retorno)


'''
def login(request):
    return render(request, "roboworld_app/login.html")

def logged_out(request):
    return render(request, "roboworld_app/logged_out.html")


def score(request):
    return render(request, "roboworld_app/score.html")
'''

def index2(request):
    return render(request,'roboworld_app/index2.html')

def proceso2(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return render(request,'roboworld_app/proceso2.html',{'name':nombre})

