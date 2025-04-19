produtos = {'Arroz': 10.00, 'Carne':12.5, 'Sabonete':3.25}

print(produtos.keys())

produto = input('Which product do you want to know the price? ')

if produto in produtos:
    print(f'The price of {produto} is {produtos[produto]}')

else:
    print('The product is not in the list.')
