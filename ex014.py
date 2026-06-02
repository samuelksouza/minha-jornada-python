lista_compras = []
item = ''
while item != 'sair':
    item = input('Digite um item: ')
    if item != 'sair':
        lista_compras.append(item)
for item in lista_compras:
    print(item)