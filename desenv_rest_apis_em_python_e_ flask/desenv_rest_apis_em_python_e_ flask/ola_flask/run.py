from flask import Flask

app = Flask(__name__)


@app.route("/<numero>", methods=['GET, POST']) # decorator
def ola():
    return 'Olá Mundo.{}'.format 

if __name__=="__main__": # se o arquivo for executado diretamente
    app.run(debug=True) # debug=True, para atualizar o servidor automaticamente
   