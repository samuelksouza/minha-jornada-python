from random import randint
numero_secreto = randint(0, 10)
chute = -1
tentativas = 0
while chute != numero_secreto:
    chute = int(input('Digite um numero de 0 a 10: '))
    tentativas += 1
    if chute == numero_secreto:
        print('Ebaa! você acertou! Número de tentativas foi {}'.format(tentativas))
    else:
        print('Errou! tente novamente')
