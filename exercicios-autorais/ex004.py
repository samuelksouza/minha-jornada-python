# Recebe a idade do usuário como um número inteiro
idade = int(input('Digite sua idade: '))

# Converte a idade para meses (multiplicando por 12 meses do ano)
idademeses = idade * 12

# Converte a idade para dias (multiplicando por 365 dias do ano, sem contar anos bissextos)
idadedias = idade * 365

# Exibe o resultado final com todas as conversões na tela
print(f'Se você tem {idade}, em meses são {idademeses} e em dias são {idadedias}')