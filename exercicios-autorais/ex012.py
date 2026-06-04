# Importa a função 'radiant' da biblioteca 'ramdom' pra gerar números aleatórios
from random import randint

# Sorteia um número secreto entre 0 até 10
numero_secreto = randint(0, 10)

# Inicializa o chute com -1 para garantir que seja diferente do número secreto no início
chute = -1

# Inicializa o contador de tentativas do jogador
tentativas = 0

# O jogo continua rodandop até que o jogador acerte o número secreto
while chute != numero_secreto:
    chute = int(input('Digite um numero de 0 a 10: '))
    tentativas += 1

    # Verifica se o jogador acertou o número
    if chute == numero_secreto:
        print('Ebaa! você acertou! Número de tentativas foi {}'.format(tentativas))
    else:
        print('Errou! tente novamente')
