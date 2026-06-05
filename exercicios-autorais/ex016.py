# Cria a lista vazia e roda o laço 5 vezes para enchê-la
lista = []
for i in range(5):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

# Exibe o maior, o menor e a soma usando as funções prontas do Python
print(f'O maior número da lista é {max(lista)}, já o menor número da lista é {min(lista)} e a soma deles é {sum(lista)} ')