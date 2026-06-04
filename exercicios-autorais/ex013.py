# Recebe a palavra que será analisada
palavra = input('Digite uma palavra: ')

# Inicializa com o contador de vogais zerado
contador = 0

# O laço 'for' percorre a string letra por letra
for letra in palavra:
    # O operador 'in' verifica de forma simples se a letra atual está dentro da string 'aeiou'
    if letra in 'aeiou':
        contador += 1

# Exibe o total de vogais encontradas na palavra digitada
print(f'existem {contador} vogais na palavra {palavra}')