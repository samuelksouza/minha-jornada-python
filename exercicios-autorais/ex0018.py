# Lista 'tarefas' vazias para guardar as que foram adicionadas
tarefas = []

# Variável para guardar as opções que o usuário escolheu (1, 2, 3, 4,)
opcao = 0

# Quando o usuário digitar o número '4' o programa sai do loop
while opcao != 4:
    # Menu de opções
    print('1 - Adiciona tarefa')
    print('2 - viualiza as tarefas')
    print('3 - Remove as tarefas')
    print('4 - Sair do programa')

    # Voltamos a variavél 'opcao' para podermos guardar a opção escolhida
    opcao = int(input('Qual a sua opcao: '))
    
    if opcao == 1:
        tarefas.append(input('Diga uma tarefa: '))
    elif opcao == 2:
        print(f'Essas são as suas tarefas: {tarefas}')
    elif opcao == 3:
        tarefas.remove(input('Diga a tarefa que deseja excluir: '))

