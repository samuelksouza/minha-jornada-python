# Inicializa uma lista para armazenar as compras e uma string vazia para controle do loop
lista_compras = []
item = ''

# O laço continua rodando até o usuário digitar a palavra 'sair'
while item != 'sair':
    item = input('Digite um item: ')

    # Valida se o item não é a palavra 'sair'
    if item != 'sair':
        lista_compras.append(item)

# O laço 'for' para percorrer a lista e exibir cada um dos itens citados
for item in lista_compras:
    print(f'- {item}') # Vai exibir: -arroz -feijão, etc.