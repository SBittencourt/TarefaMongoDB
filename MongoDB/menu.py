from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import crud_usuario
import crud_produto

key = 0
sub = 0
while (key != 'S'):
    print("1-CRUD Usuário")
    print("2-CRUD Vendedor")
    print("3-CRUD Produto")
    print("4-CRUD Compras")
    print("5-CRUD Favoritos")
    key = input("Digite a opção desejada? (S para sair) ")

    if (key == '1'):
        print("Menu do Usuário")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create usuario")
            crud_usuario.create_usuario()
            
        elif (sub == '2'):
            nomeUsuario = input("Read usuário, deseja algum nome especifico? ")
            crud_usuario.read_usuario(nomeUsuario)
        
        elif (sub == '3'):
            nomeUsuario = input("Update usuário, deseja algum nome especifico? ")
            crud_usuario.update_usuario(nomeUsuario)

        elif (sub == '4'):
            print("delete usuario")
            nomeUsuario = input("Nome a ser deletado: ")
            sobrenome = input("Sobrenome a ser deletado: ")
            crud_usuario.delete_usuario(nomeUsuario, sobrenome)
    
    
    elif (key == '2'):
        print("Menu do Vendedor")  

    elif (key == '3'):
        print("Menu do Produto") 
        print("1 - Criar Produto")
        print("2 - Ver Produto")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Criar Produto")
            crud_produto.create_produto()
            
        elif (sub == '2'):
            nomeProduto = input("Visualizar produtos, deseja algum nome especifico? Caso não, pressione enter")
            crud_produto.read_produto(nomeProduto)
        
        elif (sub == '3'):
            nomeProduto = input("Atualizar produtos, deseja algum nome especifico? ")
            crud_produto.update_produto(nomeProduto)

        elif (sub == '4'):
            print("deletar produto")
            nomeProduto = input("Nome a ser deletado: ")
            crud_produto.delete_produto(nomeProduto)

print("Tchau Prof...")