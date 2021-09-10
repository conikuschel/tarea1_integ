from django.shortcuts import render
from django.http import HttpResponse, response
import requests

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Mosh'})

def home(request):
    sigo = True
    sigo1 = True
    count =2
    count1=2
    lista =[]
    response = requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/users?_page=1').json()
    responsec = requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/cities?_page=1').json()
    while sigo==True:
        response1 = requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/users?_page={0}'.format(count)).json()
        if len(response1) == 10:
            response+=response1
            count+=1
        elif len(response1) < 10:
            response+=response1
            sigo = False
        elif len(response1) == 0:
            sigo = False 
    lista.append(response)

    while sigo1==True:
        response1c = requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/cities?_page={0}'.format(count1)).json()
        if len(response1c) == 10:
            responsec+=response1c
            count1+=1
        elif len(response1c) < 10:
            responsec+=response1c
            sigo1 = False
        elif len(response1c) == 0:
            sigo1 = False 

    lista.append(responsec)
    return render(request, 'home.html', {'response':lista})

    

def profile(request, user):
    lista = []
    response=requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/users/{0}'.format(user)).json()
    lista.append(response)
    response=requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/users/{0}/credit-cards'.format(user)).json()
    lista.append(response)
    response=requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/users/{0}/addresses'.format(user)).json()
    lista.append(response)
    return render(request, 'profile.html', {'response':lista})

def city(request, id_city):
    city = id_city.lower()
    response=requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/cities?q={0}'.format(city)).json()
    lista = response[0]['users']
    response1 = []
    lista1 = []
    response1.append(response[0])
    for i in lista:
        response2 = requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/users/{0}'.format(i)).json()
        lista1.append(response2)
    response1.append(lista1)
    return render(request, 'city.html', {'response':response1})

def busc(request):
    if request.method == "POST":
        searched = request.POST['searched2']
    response=requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/cities?q={0}'.format(searched)).json()
    return render(request, 'busqueda.html', {'response':response})

def busc1(request):
    if request.method == "POST":
        searched = request.POST['searched']

    response = requests.get('https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/26417/users?q={0}'.format(searched)).json()
    return render(request, 'busqueda1.html', {'response':response})

    