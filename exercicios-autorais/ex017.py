# Vai receber as notas
notas = []

# Essa variavél foi criada para guardar as notas que o usuário digitou, para depois serem guardadas na 'notas'
nota = 0

# Nesse loop 'while', diz que, enquanto a variavél 'nota' for diferente de '-1' o loop continua
while nota != -1:
    # Aqui a nota recebe os valores das notas
    nota = float(input('Digite a nota do aluno: '))

    # Aqui, usamos o if para verificar se a nota digitada é '-1'
    if nota != -1:
        # Aqui, a variavél 'notas' recebe o valor que o usuário colocou em 'nota', usando o .apprend
        notas.append(nota)

# Exibe a maior nota usando a função 'max', para a menor usamos a 'min' e para a média usamos primeiro o sum para somar todas as notas,
# Logo após isso usamos '/' para dividir peelo 'len' que usamos para retornar a quantidade de itens da variavel 'notas'
print(f'A maior nota foi {max(notas)}, a mneor foi {min(notas)} e a média foi {sum(notas)/len(notas)}')