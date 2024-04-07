from flask_restful import Resource
from flask import Flask, request
import json


lista_habilidades = [
    {'id':0,
    'habilidade' : 'Python'},
    
    {'id':1,
    'habilidade' : 'Java'},
    
    {'id':2,
    'habilidade' : 'PHP'},
    
    {'id':3,
    'habilidade' : 'Flask'},
]

class Habilidades(Resource):   
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados
    
    def delete(self,id):
        lista_habilidades.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluido'}
 
   
class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades
    
    def post(self):
        dados = json.loads(request.data)
        if dados['habilidade'] in [habilidade['habilidade'] for habilidade in lista_habilidades]:
            print("Habilidade já cadastrada!")
        else:
            posicao = len(lista_habilidades)
            dados['id'] = posicao
            lista_habilidades.append(dados)
            return dados