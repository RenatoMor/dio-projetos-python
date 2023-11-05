import pprint
import pymongo
import pymongo as pyM
import datetime


client = pyM.MongoClient("mongodb+srv://renatoklaver:sollua@cluster7.snzhgqx.mongodb.net/?retryWrites=true&w=majority")

db = client.banking
collection = db.banking_collection
print(db.banking_collection)
print('\n')

# Inserção de info para compor único doc----------------------------

post = {
    "nome": "Cliente",
    "cpf": "100000000",
    "endereco": ["Logradouro", "nº", "Bairro", "Estado/uf"],
    "conta": "1000",
    "saldo": "0000.00",
    "data": datetime.datetime.utcnow()
}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
print('\n')

# Recuperando informações do post------------------------------------

print(db.posts.find_one())
print('\n')
pprint.pprint(db.posts.find_one())
print(db.posts)
print('\n')
print(db.list_collection_names())
print('\n')

# Inserção em massa-------------------------------------------------

new_posts = [{
    "nome": "Fernanda Abreu",
    "cpf": "000000001",
    "endereco": ["Rua França", "77", "Vila Salermo", "Bahia/BA"],
    "conta": "0001",
    "saldo": 5000.00,
    "data": datetime.datetime.utcnow()},
    {
        "nome": "Tim Maia",
        "cpf": "000000011",
        "endereco": ["Rua Alemanha", "nº 10", "Jd. Napoles", "São Paulo/SP"],
        "conta": "0002",
        "saldo": 5000.00,
        "data": datetime.datetime.utcnow()},
    {
        "nome": "Alexandra Daddario",
        "cpf": "000000021",
        "endereco": ["Rua Bélgica ", "21", "Vila Turim", "Rio de Janeiro/RJ"],
        "conta": "0003",
        "saldo": 5000.00,
        "data": datetime.datetime.utcnow()},
    {
        "nome": "Barack Obama",
        "cpf": "000000031",
        "endereco": ["Rua Espanha", "33", "Jd. Milão", "Minas Gerais/MG"],
        "conta": "0004",
        "saldo": 5000.00,
        "data": datetime.datetime.utcnow()}]

result = posts.insert_many(new_posts)

# Recuparação de docs presentes na coleção post-----------------

print(result.inserted_ids)
print('\n')
pprint.pprint(db.posts.find_one())
print('\n')
pprint.pprint(db.posts.find_one({"nome": "Fernanda Abreu"}))
print("\n")

for post in posts.find():
    pprint.pprint(post)

# Recuperando multiplos docs------------------------------------

pprint.pprint(posts.find_one({"tags": "insert"}))
print('\n')
print(posts.count_documents({}))
print('\n')
print(posts.count_documents({'nome': 'Tim Maia'}))
print('\n')
print(posts.count_documents({'endereco': 'Vila Salermo'}))
print('\n')
for post in posts.find({}).sort('saldo'):
    pprint.pprint(posts)
print('\n')

# Recuperando info de maneira ordenada---------------------------

for post in posts.find({}).sort("date"):
    pprint.pprint(post)

print('\n')
result = db.profile.create_index([('nome', pymongo.ASCENDING)], unique=True)
print("\n")
print(sorted(list(db.profile.index_information())))
print("\n")

# Craindo um novo documento-------------------------------------

user_profile_user = [
    {"user_id": 100, "name": "Alexandre"},
    {"user_id": 101, "name": "Roger"}]

result = db.profile_user.insert_many(user_profile_user)

# Coleções armazenadas no mongoDB---------------------------------

for x in db.list_collection_names():
    print(x)

# Deleta todos os documentos do banco de dados--------------------

client.drop_database('banking')


# Deleta todos os documentos do banco de dados--------------------

db['posts'].drop()