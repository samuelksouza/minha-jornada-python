# Variavél que recebe 'input'
frase = input('Digite uma frase: ')

# Variavél que recebe 'frase' e o '.split', que divide a frase em uma lista a partir dos espaços
palavras = frase.split()

# Remove os espaços da contagem para poder contar apenas as letras
frase_sem_espaco = frase.replace(' ', '')

# Exibe quantas letras tem na frase usando o 'len'
print(f'A frase tem {len(frase_sem_espaco)} letras na frase: "{frase}"')

# Seguindo a mesmo lógica da linha de cima, uso o 'len' com a variavél 'palavras' para mostar a quantidade de palavras da frase
print(f'A quantidade de palavras na frase "{frase}" é de {len(palavras)} palavras')