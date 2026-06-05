# Cria variáveis iniciais necessárias
senha_chute = ''
senha_correta = 'python123'

# Repete o bloco enquanto a senha digitada for errada
while senha_chute != senha_correta:
    senha_chute = input('Digite a sua senha: ')

    # Avisa se a senha digitada for a errada
    if senha_chute != senha_correta:
        print('Senha incorreta')

# Só executa essa  lina quando o usuário digita a senha correta e saí do While
print('Senha correta')