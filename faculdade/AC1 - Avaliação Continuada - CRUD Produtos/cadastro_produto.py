
produtos = []

def AdicionarProduto(produtos):
    print('\n\nADICIONAR PRODUTO')
    descricao = input('Descrição produto:')
    preco = float(input('Preço produto:'))
    produto = {'descricao': descricao, 'preco': preco}
    produtos.append(produto)
    print('Produto cadastrado com sucesso:')
    print(f"${produto['descricao']} ... R$ ${produto['preco']} \n\n")


def ListarProdutos(produtos):
    print('\n\nLISTA DE PRODUTO')
    for produto in produtos:
        print(f'${produto["descricao"]} ... ${produto["preco"]}')
    print('\n\n')


def EditarProdutos(produtos):
    print('\n\nEDITAR PRODUTO')
    for produto in produtos:
        print(f'${produto["descricao"]} ... ${produto["preco"]}')

    produtoedit = input("Digite exatamente a descrição do produto que quer editar: ").strip()

    precoedit = float(input("Digite o novo preço do produto: ").strip())

    for produto in produtos:
        if produto["descricao"] == produtoedit:
            print("Produto encontrado!")

            produto["preco"] = precoedit
            break
    else:
        print("Produto não encontrado!")


def DeletarProdutos(produtos):
    print('\n\nDELETAR PRODUTO')
    for produto in produtos:
        print(f'${produto["descricao"]} ... ${produto["preco"]}')

    produtoremove = input("Digite exatamente a descrição do produto que quer deletar: ").strip()

    for i, produto in enumerate(produtos):

        if produto["descricao"] == produtoremove:

            print("Produto encontrado!")

            produtos.pop(i)

            print("Produto excluído com sucesso!")

            break
    else:
        print("Produto não encontrado!")


while True:
    print('CADASTRO PRODUTOS')
    print('--------------------')
    print('1 - Adicionar produto') # C - Create
    print('2 - Listar produtos')   # R - Read
    print('3 - Editar produto')    # U - Update
    print('4 - Deletar produto')   # D - Delete
    print('--------------------')
    print('0 - Sair')
    print('--------------------')

    opcao = int(input('Digite a opção deseja:'))

    if opcao == 0:
        break

    elif opcao == 1:
        AdicionarProduto(produtos)

    elif opcao == 2:
        ListarProdutos(produtos)

    elif opcao == 3:
        EditarProdutos(produtos)

    elif opcao == 4:
        DeletarProdutos(produtos)
