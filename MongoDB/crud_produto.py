from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://silmara:123@cluster0.05p7qyc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercadolivre

def delete_produto(nome):
    global db
    mycol = db.produto
    myquery = {"nome": nomeProduto}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o produto ",mydoc)

def create_produto():
    global db
    mycol = db.produto
    print("\nInserindo um novo produto")
    nomeProduto = input("Nome: ")
    preco = float(input("Preço: "))
    marca = input("Marca: ")
    
    mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"],x["cpf"])

    mydoc = { "nome": nomeProduto, "preço": preco, "marca": marca, "end": end }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)

def read_produto(nomeProduto):
    global db
    mycol = db.produto
    print("Usuários existentes: ")
    if not len(nomeProduto):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"])
    else:
        myquery = {"nome": nomeProduto}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_produto(nomeProduto):
    #Read
    global db
    mycol = db.produto
    myquery = {"nomeProduto": nome}
    mydoc = mycol.find_one(myquery)
    print("Dados do produto: ",mydoc)
    nomeProduto = input("Mudar nome do produto:")
    if len(nome):
        mydoc["nome"] = nomeProduto

    preco = float(input("Mudar preço:"))
    if len(cpf):
        mydoc["Preço"] = preco


    marca = input("Mudar marca:")
    if len(marca):
        mydoc["marca"] = marca

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)
      