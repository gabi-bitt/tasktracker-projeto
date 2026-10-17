"""TaskTracker - gerenciador de tarefas em linha de comando."""

tarefas = []


def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def cadastrar_tarefa():
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade (Alta, Média ou Baixa): ")
    data_limite = input("Data limite (DD/MM/AAAA): ")
    tarefas.append({
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    })
    print("Tarefa cadastrada com sucesso!")


def visualizar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa cadastrada no momento.")
        return
    for i, t in enumerate(tarefas, start=1):
        print(f"\nTarefa {i}")
        for campo, valor in t.items():
            print(f"  {campo}: {valor}")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
