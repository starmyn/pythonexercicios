listas_produtos = []
categorias = ['frutas', 'bebidas']
num_produtos = int(input('Quantos produtos voce deseja adicionar? '))

for i in range(num_produtos):
    produto = input('Nome dos Produtos: ')
    quantidade = int(input('Quantidade: '))
    listas_produtos.append([produto, quantidade])

print("Lista de compras:")
for produtos, quantidade in listas_produtos:
    print(f"Produto: {produto} - Qtd: {quantidade}")