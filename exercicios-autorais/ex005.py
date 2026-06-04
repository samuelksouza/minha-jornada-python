# Recebe o número inteiro do qual o usuário deseja ver a tabuada
numero = int(input('Digite um numero inteiro: '))

# Cria um laço que vai repetir 10 vezes.
# O range(1, 11) começa no 1 e para antes do 11 (ou seja, vai de 1 até 10)
for i in range(1, 11):
    # Exibe a linha da tabuada calculando o resultado direto na f-string
    print(f'{numero} x {i} = {numero * i}')