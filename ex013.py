palavra = input('Digite uma palavra: ')
contador = 0
for letra in palavra:
    if letra in 'aeiou': #or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        contador += 1
print(f'existem {contador} vogais na palavra {palavra}')