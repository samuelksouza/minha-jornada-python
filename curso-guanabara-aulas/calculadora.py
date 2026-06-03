#Calculadora em Python

#Variavéis
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo  numero: '))
num3 = int(input('Digite o terceiro numero: '))

operacao = input('digite a operação ')

#Match case para selecionar a operação
match operação:
    case '+':
        res = num1 + num2 + num3
    case '-':
        res = num1 - num2 - num3
    case '*':
        res = num1 * num2 * num3
    case '/':
        res = num1 / num2 / num3

#Print para mostrar o resultado da operação
#F string para colocar a variavél dentro do texto
print ('O resultado é  {}'. format(res))