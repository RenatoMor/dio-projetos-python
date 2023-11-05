from flask import Flask

app = Flask(__name__)


@app.route("/") # decorator
def ola():
    return 'Olá Mundo.'

if __name__=="__main__": # se o arquivo for executado diretamente
    app.run(debug=True) # debug=True, para atualizar o servidor automaticamente 