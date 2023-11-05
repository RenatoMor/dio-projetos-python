from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import inspect
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

'''
Base declarativa é uma classe que mantém um catálogo de classes 
de domínio e mapeia essas classes para tabelas de banco de dados.
'''
Base = declarative_base()

# Cliente---------------------------------------------------------------------
class Cliente(Base):
    # Nome da Tabela
    __tablename__ = 'cliente'
    # Atributos que correspondem às colunas do banco de dados.
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(40))
    cpf = Column(Integer, unique=True)
    email = Column(String(30), unique=True)
    endereco = Column(String(40))

    # relationship é uma função que define um relacionamento entre duas classes.
    conta = relationship("Conta", back_populates="cliente", cascade="all, delete-orphan")

    # __repr__ é uma representação de string de um objeto.
    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, " \
               f"cpf={self.cpf}, email={self.email}, endereco={self.endereco}"

# Conta-----------------------------------------------------------------------
class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(15))
    agencia = Column(Integer, unique=False)
    conta = Column(Integer, unique=True)
    saldo = Column(Float)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)

    cliente = relationship(
        "Cliente", back_populates="conta"
    )


    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, " \
               f"agencia={self.agencia}, conta={self.conta}, saldo={self.saldo}) "

# ----------------------------------------------------------------------------

print(Conta.__tablename__)
print(Cliente.__tablename__)

# Conexão com o banco de dados------------------------------------------------
engine = create_engine('sqlite://')

# Criando as classes como tabelas no banco de dados---------------------------
Base.metadata.create_all(engine)

print('===Investiga o esquema do banco de dados===')
inspector_engine = inspect(engine)

print(inspector_engine.has_table('Cliente'))
print(inspector_engine.get_table_names())
print(inspector_engine.default_schema_name)

print('\n')

# Persistir dados no sqlite---------------------------------------------------
with Session(engine) as session:
    fernanda = Cliente(
        nome='Fernanda Abreu',
        cpf="100000001",
        endereco='Logradouro - nº - Bairro - Estado/UF',
        email='fernandaa@gmail.com',
    )
    conta_fernada = Conta(
        agencia='0001',
        conta='0001',
        tipo='conta_corrente',
        saldo=5000.00,
        cliente=fernanda,
    )
    tim = Cliente(
        nome='Tim Maia',
        cpf='100000011',
        email='timm@gmail.com',
        endereco='Logradouro - nº - Bairro - Estado/UF',
    )
    conta_tim = Conta(
        agencia='0001',
        conta='0002',
        tipo='conta_corrente',
        saldo=5000.00,
        cliente=tim,
    )

    alexandra = Cliente(
        nome='Alexandra Daddario',
        cpf='100000021',
        email='alexandrad@gmail.com',
        endereco='Logradouro - nº - Bairro - Estado/UF',
    )
    conta_alexandra = Conta(
        agencia='0001',
        conta='0003',
        tipo='conta_corrente',
        saldo=5000.00,
        cliente=alexandra,
    )

    barack = Cliente(
        nome='Barack Obama',
        cpf='100000031',
        email='baracko@gmail.com',
        endereco='Logradouro - nº - Bairro - Estado/UF',
    )
    conta_barack = Conta(
        agencia='0001',
        conta='0004',
        tipo='conta_corrente',
        saldo=5000.00,
        cliente=barack,
    )


# Recuperar dados-------------------------------------------------------------
    session.add_all([fernanda, conta_fernada, tim, conta_tim,
                     alexandra, conta_alexandra, barack, conta_barack])

    session.commit()
print('=====Recuperando com filtro utilizando a clausula where=====')
stmt = select(Cliente).where(Cliente.nome.in_(['Fernanda Abreu', 'Tim Maia',
                                               'Alexandra Daddario', 'Barack Obama']))
for cliente in session.scalars(stmt):
    print(cliente)

print('\n')

print("=====Recuperando info com order_by em ordem decrescente=====")
stmt_order = select(Cliente).order_by(Cliente.nome.desc())
for result in session.scalars(stmt_order):
    print(result)

#Pesquisas executando stmt a partir da connction------------------------------

connection = engine.connect()

print('===Recuperando info .join/session.scalars===')
stmt_join = select(Cliente.nome, Conta.tipo).join_from(Cliente, Conta)
for result in session.scalars(stmt_join):
    print(result)

print('\n')

print('===Recuperando info com join/fetchall===')
result = connection.execute(stmt_join).fetchall()
for result in result:
    print(result)

print('\n')

print('===Recuperando info com .join/.fetchmany===')
result = connection.execute(stmt_join).fetchmany(2)
for result in result:
    print(result)

print('\n')

print('======Total de instâncias em Cliente======')
stmt_count = select(func.count('*')).select_from(Cliente)
for result in session.scalars(stmt_count):
    print(result)

print('==========================================')
