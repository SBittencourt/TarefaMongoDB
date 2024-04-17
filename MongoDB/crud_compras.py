from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://silmara:123@cluster0.05p7qyc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercadolivre

def listar_produtos():
    global db
    print("Lista de produtos:")
    produtos = list(db.produto.find())
    for i, produto in enumerate(produtos, start=1):
        vendedor = db.vendedor.find_one({"cpf": produto.get("vendedor")})
        if vendedor:
            print(f"{i} - ID: {produto['_id']} | Produto: {produto['nome']} | Vendedor: {vendedor['nome']} | Preço: {produto['preço']}")
        else:
            print(f"{i} - ID: {produto['_id']} | Produto: {produto['nome']} | Vendedor: Não disponível | Preço: {produto['preço']}")


def adicionar_carrinho(cpf_usuario):
    global db
    carrinho = []
    while True:
        print("\nLista de produtos disponíveis:")
        listar_produtos()

        id_produto = input("\nDigite o número do produto que deseja adicionar ao carrinho (ou 'C' para concluir): ")
        if id_produto.upper() == 'C':
            break

        try:
            id_produto = int(id_produto)
            produtos = list(db.produto.find())
            if id_produto < 1 or id_produto > len(produtos):
                raise ValueError
            produto = produtos[id_produto - 1]
            carrinho.append(produto)
            print(f"Produto '{produto['nome']}' adicionado ao carrinho.")
        except ValueError:
            print("Erro: Produto inválido. Digite um número válido.")

    if not carrinho:
        print("Carrinho vazio. Operação cancelada.")
    
    return carrinho


def visualizar_carrinho(carrinho):
    if not carrinho:
        print("Carrinho vazio.")
        return
    
    print("\nProdutos no carrinho:")
    total = 0
    for i, produto in enumerate(carrinho, start=1):
        if isinstance(produto, dict):  # Verificar se produto é um dicionário
            total += produto.get("preço", 0)  # Usar get para acessar o preço do produto
            print(f"{i} - Nome do Produto: {produto.get('nome')} | Preço: {produto.get('preço')}")
        else:
            print("Erro: Produto inválido encontrado no carrinho.")
    
    print("\nTotal a pagar:", total)



def editar_carrinho(carrinho):
    if not carrinho:
        print("Carrinho vazio. Não há itens para editar.")
        return

    while True:
        print("\nOpções de edição:")
        print("1 - Remover produto do carrinho")
        print("2 - Voltar")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            visualizar_carrinho(carrinho)
            indice = input("Digite o número do produto que deseja remover (ou 'V' para voltar): ")
            if indice.upper() == 'V':
                break

            try:
                indice = int(indice)
                if 1 <= indice <= len(carrinho):
                    carrinho.pop(indice - 1)
                    print("Produto removido do carrinho com sucesso.")
                else:
                    print("Número de produto inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

        elif opcao == '2':
            break
        else:
            print("Opção inválida. Digite '1' para remover um produto ou '2' para voltar.")

def concluir_compra(cpf_usuario, carrinho):
    if not carrinho:
        print("Carrinho vazio. Não é possível concluir a compra.")
        return

    print("\nProdutos no carrinho:")
    total = 0
    for i, produto in enumerate(carrinho, start=1):
        total += produto["preço"]
        print(f"{i} - Nome do Produto: {produto['nome']} | Preço: {produto['preço']}")

    print("\nTotal a pagar:", total)

    while True:
        confirmar = input("Deseja confirmar a compra (S/N)? ").upper()
        if confirmar == "S":
            print("Compra concluída com sucesso!")
            return carrinho
        elif confirmar == "N":
            print("Compra cancelada.")
            return carrinho
        else:
            print("Opção inválida. Por favor, digite 'S' para confirmar ou 'N' para cancelar.")
