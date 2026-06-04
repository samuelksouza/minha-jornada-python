# 'n1' e 'n2' usam a função input para receber o valor eestão dentro de um int pra determinar que é um valor inteiro
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor: '))

# 'op' também recebe int para que o resultado da operação seja um valor inteiro
op = int(n1 + n2)

# exibe a soma das variaveis e usa fstring
print(f'A soma entre {n1} e {n2} é {op}')