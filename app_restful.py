from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, ListaHabilidades, lista_habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':0,
    'nome':'Rafael',
     'habilidades':['Python', 'Flask']
     },
    {'id':1,
    'nome':'Galleani',
     'habilidades':['Python', 'Django']
     }
]

# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, Procure o administrador da API'
            response = {'status':'erro', 'mensagem': mensagem}        
        return (response)
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return (dados)
    
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluido'}

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        dados_alter = dados["habilidades"]
        ocorrencias_nao_encontradas = []
        for ocorrencia in dados_alter:
            if not any(ocorrencia in dicionario.values() for dicionario in lista_habilidades):
                ocorrencias_nao_encontradas.append(ocorrencia)
        
        if ocorrencias_nao_encontradas:    
            return {'status':'falha', 'mensagem':'Habilidades {} não cadastradas!'.format(', '.join(ocorrencias_nao_encontradas))}
        else:
            posicao = len(desenvolvedores)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            return desenvolvedores[posicao]
        

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:id>/')
api.add_resource(ListaHabilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)