# Inicializa as variáveis: "Soma" começa zerada e "número" começa com 1 para conseguir entrar no laço
soma = 0
numero = 1

# O laço vai continuar ENQUANTO o número digitado for diferente de 0
while numero != 0:
    numero = int(input('Digite um numero: '))
    # Soma acumulativa: pega o valor atual de "soma" e adiciona o "número" digitado
    soma += numero

# Quando o usuário digita 0, o laço fecha e o total acumulado é mostrado
print(f'A soma de todos os números é {soma}')