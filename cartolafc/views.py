import json
import requests
from django.shortcuts import render
from models import *

def index(request):
    
    liga=Liga('teamoangelim')
    
    try:
        liga.obter_times()
    except (Exception) as erro:
        imp=erro
        msg='Servidores ocupados, atualize novamente em instantes!'
        print imp
        return render(request,'index.html',{"erro" : msg})
    return render(request,'index.html',{"liga" : liga.lista_times})

#time=Time('macunaima','jorge henrique','','','3','1','100',Atleta.criar_atleta())
    #print macunaima.lista_atletas[1].nome    
    #, { "atleta" : time.lista_atletas}

