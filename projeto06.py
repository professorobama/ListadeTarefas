#Lista de Tarefas:
#Desenvolva um aplicativo simples de lista de tarefas onde o usuário pode adicionar, remover e visualizar suas tarefas. Use um laço de repetição for para exibir a lista de tarefas.

# Função para adicionar uma tarefa à lista
def adicionar_tarefa(lista_tarefas, tarefa):
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para remover uma tarefa da lista
def remover_tarefa(lista_tarefas, indice):
    if indice >= 0 and indice < len(lista_tarefas):
        tarefa_removida = lista_tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Índice inválido. Tarefa não removida.")

# Função para exibir a lista de tarefas
def exibir_tarefas(lista_tarefas):
    if lista_tarefas:
        print("Lista de Tarefas:")
        for indice, tarefa in enumerate(lista_tarefas):
            print(f"{indice + 1}. {tarefa}")
    else:
        print("Lista de tarefas vazia.")

# Lista inicial de tarefas
lista_tarefas = []

# Loop principal do aplicativo
while True:
    print("\n--- Lista de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Exibir Tarefas")
    print("4. Sair")

    # Solicita a escolha do usuário
    escolha = input("Escolha uma opção: ")

    # Executa a ação correspondente à escolha do usuário
    if escolha == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        adicionar_tarefa(lista_tarefas, tarefa)
    elif escolha == "2":
        if lista_tarefas:
            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
            remover_tarefa(lista_tarefas, indice)
        else:
            print("Não há tarefas para remover.")
    elif escolha == "3":
        exibir_tarefas(lista_tarefas)
    elif escolha == "4":
        print("Saindo do aplicativo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

#Este código define três funções principais: adicionar_tarefa, remover_tarefa e exibir_tarefas, que permitem ao usuário adicionar, remover e visualizar tarefas, respectivamente. O loop principal do aplicativo permite que o usuário escolha entre essas opções e saia do aplicativo.


'''Explpicando o projeto passo a passo:


1) Definição das Funções:
- Adicionar_tarefa(lista_tarefas, tarefa): Esta função recebe uma lista de tarefas e uma nova tarefa como entrada e adiciona a nova tarefa à lista.
- Remover_tarefa(lista_tarefas, indice): Esta função recebe uma lista de tarefas e um índice como entrada e remove a tarefa correspondente ao índice da lista, se existir.
- Exibir_tarefas(lista_tarefas): Esta função recebe uma lista de tarefas como entrada e imprime todas as tarefas da lista na saída padrão.

2) Loop Principal do Aplicativo:
- O loop while True: cria um loop infinito que continuará sendo executado até que o usuário decida sair do aplicativo.
- Dentro do loop, o menu principal do aplicativo é exibido, apresentando as opções disponíveis para o usuário: adicionar tarefa, remover tarefa, exibir tarefas e sair.
- O programa solicita ao usuário que escolha uma opção digitando o número correspondente ao menu.
- Dependendo da escolha do usuário, uma das funções definidas anteriormente será chamada para executar a ação desejada.
- Se o usuário escolher a opção "Sair", o loop é interrompido com a instrução break e o programa termina.

3) Manipulação das Tarefas:
- As funções adicionar_tarefa e remover_tarefa manipulam a lista de tarefas de acordo com as ações do usuário, enquanto a função exibir_tarefas apenas imprime as tarefas na tela.
- O usuário pode adicionar novas tarefas, remover tarefas existentes especificando o índice da tarefa a ser removida ou exibir todas as tarefas atualmente na lista.

Este código é um exemplo simples de um aplicativo de lista de tarefas que permite ao usuário interagir com a lista através de um menu simples, utilizando funções para realizar as operações de adição, remoção e exibição de tarefas.'''