# Recebe o número inteiro que o usuário quer testar
numero = int(input('Digite um valor para descobrir se ele é ímpar ou par: '))

# Se o resto da divisão do número por 2 for igual a zero, significa que ele é par
if numero % 2 == 0:
    print(f'{numero} é par!')
# Caso contrário (se o resto for 1), o número é ímpar
else:
    print(f'{numero} é ímpar!')