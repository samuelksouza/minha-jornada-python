# Recebe a nota do aluno permitindo números decimais (ex: 7.5) usando float
nota = float(input('Insira a nota do aluno: '))

# Se a nota for 6.0 ou qualquer valor acima, o aluno passa
if nota >= 6:
    print('Aluno aprovado')
# Se não for maior ou igual a 6, por exclusão (else), o aluno está reprovado
else:
    print('Aluno reprovado')