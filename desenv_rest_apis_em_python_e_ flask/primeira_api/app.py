from flask import Flask
from flask import jsonify
from flask import request
import json


app = Flask(__name__)

@app.route('/<int:id>/')
def pessoa(id):
    return jsonify({'id': id, 'nome': 'Luiz', 'profissao': 'programador'})
    

'''@app.route('/soma/<int:valor1>/<int:valor2>/')
def soma(valor1, valor2):
    soma = valor1 + valor2
    return jsonify({'soma': soma})'''

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])

    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})       
    

if __name__ == '__main__':
    app.run(debug=True)
