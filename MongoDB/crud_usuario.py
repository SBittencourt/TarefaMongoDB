from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://silmara:123@cluster0.05p7qyc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercadolivre

def delete_usuario(nome, sobrenome):
    global db
    mycol = db.usuario
    myquery = {"nome": nome, "sobrenome":sobrenome}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o usuário ",mydoc)

def create_usuario():
    global db
    mycol = db.usuario
    print("\nInserindo um novo usuário")
    nomeUsuario = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    key = 1
    end = []
    while (key != 'N'):
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {       
            "rua":rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco) 
        key = input("Deseja cadastrar um novo endereço (S/N)? ")
    mydoc = { "nome": nomeUsuario, "sobrenome": sobrenome, "cpf": cpf, "end": end }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)

def read_usuario(nomeUsuario):
    global db
    mycol = db.usuario
    print("Usuários existentes: ")
    if not len(nomeUsuario):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"],x["cpf"])
    else:
        myquery = {"nome": nomeUsuario}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_usuario(nomeUsuario):
    global db
    mycol = db.usuario
    myquery = {"nome": nomeUsuario}
    mydoc = mycol.find_one(myquery)
    print("Dados do usuário: ",mydoc)
    nome = input("Mudar Nome:")
    if len(nome):
        mydoc["nome"] = nomeUsuario

    sobrenome = input("Mudar Sobrenome:")
    if len(sobrenome):
        mydoc["sobrenome"] = sobrenome

    cpf = input("Mudar CPF:")
    if len(cpf):
        mydoc["cpf"] = cpf

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)
      

