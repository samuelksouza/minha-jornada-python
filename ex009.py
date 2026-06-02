n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo: '))
operacao = input("Escolha a operação(+, -, %, *): ")
if operacao == '+':
    print(n1 + n2)
if operacao == '-':
    print(n1 - n2)
if operacao == '*':
    print(n1 * n2)
if operacao == '%':
    print(n1 % n2)