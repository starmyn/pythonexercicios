produtos ={}
interação=0
while True:
    interação+=1
    produto=(input(f'digite o {interação}º produto: '))
    valor_uni=float(input(f'qual o valor unitario do profuto? '))
    quantidade_item=int(input(f'quantos {produto} você deseja comprar? '))
    produtos.update({interação:[produto, valor_uni, quantidade_item]})

    loop=(input('perfeito, você deseja adicionar mais itens?(S/N)'))
    if loop.upper()=='N':
        break

total=0

print(50 * '-')
print('lista de compras')
print(50 * '-')

for interação, produto in produtos.items():
    subtotal=produto[1] * produto[2]
    print(f'{produto[0]} - R$ {produto[1]:.2f} un - R$ {subtotal:.2f}')
    total+=subtotal

print(50 * '-')
print(f'Total da compra: R$ {total:.2f}')
print(50 * '-')





