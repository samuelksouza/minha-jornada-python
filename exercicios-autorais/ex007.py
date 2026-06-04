# Recebe três números inteiros diferentes do usuário
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
n3 = int(input('Digite o terceiro valor:'))

# Primeira verificação: testa se n1 é o maior de todos
if n1 >= n2 and n1 >= n3:
    print(f'{n1} é o maior...')

# Segunda verificação: só roda se a primeira for falsa. Testa se n2 é o maior
elif n2 >= n1 and n2 >= n3:
    print(f'{n2} é o maior...')

# Caso base: se n1 e n2 não forem os maiores, por exclusão, o n3 com certeza é o maior
else:
    print(f'{n3} é o maior...')