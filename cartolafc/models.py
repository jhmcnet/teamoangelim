import operator
from operator import itemgetter
from django.db import models
import json
import requests

class Liga(object):
    
    #arquivo=['CYROSE-2015','macunaima-soccer','mddrl','bruno-mineiro','shiruncfc2','jorrante-fc','el-secador','jrBarcana','Cortez-Uniao-FC',
    #         'MVCJESUS','Btas-FC','Los-Bucaneros-FC','mardonio-neves-lima','KDINHO-ROOTS-FC','Essa-eu-paguei','BaymaFC','kbca-fc-12','Guima-City',
    #         'Bola-de-Munique']
    arquivo=['28204028','36174527','28472745','23625239','28539359','32019377','50888277','33180073','31546587',
             '50886557','28312391','59973661','29305249','47663798','47642175','56718568','54248149','60654258','56661382']
    def __init__(self,nome):
        self.nome=nome
        self.lista_times=[]# <== A LIGA
        self.times_ordenados=[]
        
    def obter_times(self):
                
        for nome_time in self.arquivo:
            #url='http://api.cartola.globo.com/time_adv/'+nome_time+'.json'
            url='http://api.cartola.globo.com/time_adv/cadun/'+str(nome_time)+'.json'
            r=requests.get(url)
            
            arquivo_dic = json.loads(r.content)
            dados = arquivo_dic['time']
                    
            self.lista_times.append(Time(dados.get('nome'),dados.get('nome_cartola'),dados.get('imagens_escudo').get('img_escudo_32x32'),                               dados.get('imagens_escudo').get('img_escudo_160x160'),dados.get('esquema'),dados.get('patrimonio'),float(dados.get('pontuacao')),
            dados.get('cadun_id')))
                                    
        for time in self.lista_times:
            time.obter_atletas(time.cadun_id)
        
        self.lista_times.sort(key=operator.attrgetter('pontuacao'),reverse=True)
        
        for time in self.lista_times:# <==testa no console
            print   'Time %s, pontuacao %s e cartoleiro %s E ID %s' %(time.nome,time.pontuacao,time.nome_cartola,time.cadun_id) 
    
class Time(object):
    
    def __init__(self,nome='',nome_cartola='',escudo_pequeno='', escudo_grande='',esquema='',patrimonio='',pontuacao='',cadun_id=''):
        self.nome=nome
        self.nome_cartola=nome_cartola
        self.escudo_pequeno=escudo_pequeno
        self.escudo_grande=escudo_grande
        self.esquema=esquema
        self.patrimonio=patrimonio
        self.pontuacao=pontuacao
        self.cadun_id=cadun_id
        self.lista_atletas=[] #<== O TIME PROPRIAMENTE
        
    def obter_atletas(self,cadun_id):
        url='http://api.cartola.globo.com/time_adv/cadun/'+str(cadun_id)+'.json'
        r=requests.get(url)
        arquivo_dic = json.loads(r.content)
        dados = arquivo_dic['atleta']
        
        
        for x in range(0,len(dados)):
            escudo=dados[x].get('clube').get('escudo_pequeno')
            posicao=dados[x].get('posicao').get('abreviacao')
            apelido=dados[x].get('apelido')
            pontos=dados[x].get('pontos')
            self.lista_atletas.append(Atleta(escudo,posicao,apelido,pontos))
        
 
        
class Atleta(object):
    def __init__(self,escudo='',posicao='',nome='',pontuacao=''):
        self.escudo=escudo
        self.posicao=posicao
        self.nome=nome
        self.pontuacao=pontuacao
   
        
    


        