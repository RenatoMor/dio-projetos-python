from flask import Flask
from flask import jsonify
from flask import request
import json

"""Cadastro de tarefas:
    • Desenvolva uma API que gerencie um cadastro de tarefas.

    • A API terá os seguintes campos:
        - id (int)
        - responsável (string)
        - descricao (string)
        - status (string)
        
    • A API deverá permitir:
        - Listar todas as tarefas
        - Incluir uma nova tarefa        
        - Uma tarefa através do id
        - Alterar o status de uma tarefa
        - Excluir uma tarefa
        - Nenhuma outra alteração deverá ser permitida além do status da tarefa.
"""

app_tarefas = Flask(__name__)

tarefas = [
    {
        'id': 0,
        'responsavel': 'Renato',
        'descricao': 'Estudar Python',
        'status': 'Em andamento'
    },
    {
        'id': 1,
        'responsavel': 'Eduarda',
        'descricao': 'Estudar Flask',
        'status': 'Finalizado'
    },
    {
        'id': 2,
        'responsavel': 'Fernando',
        'descricao': 'Estudar Django',
        'status': 'Iniciar'
        
    }

]

#> Devolve tarefa pelo ID, altera e deleta
@app_tarefas.route('/tarefa/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = f'Tarefa de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}      
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)
    
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})


#> Lista todas as tarefas e permite registrar uma nova tarefa
@app_tarefas.route('/tarefa/', methods=['POST', 'GET'])
def listar_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
    
    elif request.method == 'GET':
        return jsonify(tarefas)
    
if __name__ == '__main__':
    app_tarefas.run(debug=True)

# Alterar o o projeto e atualizar o GitHub



