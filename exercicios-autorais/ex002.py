# Lê os valores do teclado e os converte de texto (str) para número inteiro (int)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

# Realiza a operação aritmética de adição entre os dois números
soma = n1 + n2

# Exibe o resultado na tela usando f-string para interpolar as variáveis direto no texto
print(f'Asoma entre {n1} e {n2} é {soma}')