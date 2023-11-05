from flask import Flask
from flask import jsonify
from flask import request
import json


app = Flask(__name__)
 

@app.route('/<int:id>') # decorator
def pessoa(id):
    soma = 1 + id
    return jsonify({'id': id, 'nome': 'Renato', 'profissao': 'Desenvolvedor'})

'''@app.route('/soma/<int:valor1>/<int:valor2>')
def soma(valor1, valor2):
    return {'soma' : valor1 + valor2}'''

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma':total})


if __name__=="__main__": # se o arquivo for executado diretamente
    app.run(debug=True) # debug=True, para atualizar o servidor automaticamente