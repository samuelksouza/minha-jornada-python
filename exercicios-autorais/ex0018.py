# Lista 'tarefas' vazia pra guardar as que foram adicionadas
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

    # Usamos o 'try' para TENTAR executar um bloco que pode gerar erro se o usuário digitar uma letra
    try :
        # Voltamos a variavél 'opcao' para podermos guardar a opção escolhida
        opcao = int(input('Qual a sua opcao: '))

    # Se o usuário digitar uma letra, o Python gera um 'ValueError'
    except ValueError:
        print('Opção invalida! Por favor, digite apenas números. (1, 2, 3 ou 4)')

        # O 'continue' faz o Python ignorar o resto dos 'if/elif' abaixo e voltar direto para o início do 'while'
        continue
    # Se a 'opcao' for igual a '1', usamos '.append' para adicionar um objeto na variavél 'tarefas'
    if opcao == 1:
        tarefas.append(input('Diga uma tarefa: '))

    # Se a 'opcao' for igual a '2', usamos o 'print' com fstring para mostrar a variavél dentro de um texto
    elif opcao == 2:
        print(f'Essas são as suas tarefas: {tarefas}')

    # Se a 'opcao' for igual a '3'...
    elif opcao == 3:

        # Mostra as tarefas que estão salvas
        print(f'tarefas: {tarefas}')

        # Nova variavél que usa input para o usuário escolher a tarefa pra remover
        tarefa_para_remover = input('Qual a tarefa que deseja remover? : ')

        # Se a tarefa escolhida estiver dentro da variavél 'tarefas'...
        if tarefa_para_remover in tarefas:

            # 'tarefas' com '.remove' recebe entre parêteses a variavél 'tarefas_para_remover'
            tarefas.remove(tarefa_para_remover)

            # Print para mostrar que a tarefa foi removida com sucesso!
            print('Tarefa removida!')