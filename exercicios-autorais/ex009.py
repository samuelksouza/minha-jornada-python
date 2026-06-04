# Recebe os dois números para fazer a operação
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo: '))

# Captura o símbolo da operação desejada
operacao = input("Escolha a operação(+, -, %, *): ")

# Verifica Qual foi a operação escolhida e faz e operação mostrando o resultado
if operacao == '+':
    print(f'resultado {n1 + n2}')
elif operacao == '-':
    print(f'resultado {n1 - n2}')
elif operacao == '*':
    print(f'resultado {n1 * n2}')
elif operacao == '%':
    print(f'resultado {n1 % n2}')