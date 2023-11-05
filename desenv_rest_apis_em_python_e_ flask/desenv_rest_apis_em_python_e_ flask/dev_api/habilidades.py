from flask_restful import Resource
from flask import request
import json


lista_habilidades = ['Python', 'Java', 'Flask', 'django', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    
    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados)
        return lista_habilidades[-1]
    
    def put(self):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self):
        lista_habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}
        

    