from models import Pessoas


def insere_pessoa():
    pessoa = Pessoas(nome='Paula', idade=23)
    print(pessoa)
    pessoa.save()


def consulta_pessoa():
    # pessoa = Pessoas.query.all()
    # print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Juliana').first()
    print(pessoa)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Julia').first()
    pessoa.nome = 'Juliana'
    pessoa.save() 


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Renato').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoa()
    consulta_pessoa() 
    # altera_pessoa()
    # exclui_pessoa()
