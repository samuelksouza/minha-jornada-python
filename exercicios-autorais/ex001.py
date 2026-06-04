# Interação básica: Captura o nome do usuário e exibe uma mensagem personalizada de boas-vindas
# Solicita o nome do usuário através do terminal e armazena o texto na variável 'nome'
nome = input('Digite o seu nome: ')

# Exibe a mensagem de boas-vindas, usando o método .format() para inserir o nome dentro das chaves {}
print('Olá {}, seja bem vindo!'.format(nome))