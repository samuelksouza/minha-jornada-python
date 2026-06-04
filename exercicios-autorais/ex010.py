# Contagem regressiva
# Importa a biblioteca "time" para poder usar funções que estão relacionadas ao tempo
import time

# O lanço começa no 10, para antes do - (ou seja, vai até o 0) e o terceiro parâmetro (-1) indica que vai subtraindo de 1 em 1
for i in range(10, -1, -1):
    print(i)

    # Faz o código pausar a execução por 1 segundo antes de ir para o próximo número
    time.sleep(1)

# Mensagem exibida após o término do laço de repetição
print('Sua contagem chegou ao fim!')