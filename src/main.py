"""TaskTracker - gerenciador de tarefas em linha de comando.

Bootcamp II - Fase 2 (Entrega Intermediária).
Autora: Gabriela Oliveira Bittencourt
"""

from datetime import date, datetime

# Lista em memória que armazena todas as tarefas (cada tarefa é um dicionário).
tarefas = []

# Prioridades aceitas (chave em minúsculo -> valor padronizado) e ordem de exibição.
PRIORIDADES_VALIDAS = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}
ORDEM_PRIORIDADE = {"Alta": 0, "Média": 1, "Baixa": 2}


# ----------------------------- Validações -----------------------------
def ler_titulo():
    """Pede o título até que um valor não vazio (e não só espaços) seja informado."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O título é obrigatório e não pode ficar vazio.")


def ler_prioridade():
    """Pede a prioridade até receber Alta, Média/Media ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("[ERRO] Prioridade inválida. Digite exatamente: Alta, Média ou Baixa.")


def converter_data(texto):
    """Converte 'DD/MM/AAAA' em date. Retorna None se não estiver nesse formato."""
    try:
        return datetime.strptime(texto, "%d/%m/%Y").date()
    except ValueError:
        return None


def ler_data_limite(data_criacao):
    """Pede a data limite. Aceita formato livre ou DD/MM/AAAA.

    Se estiver no formato DD/MM/AAAA, não pode ser anterior à data de criação.
    """
    while True:
        texto = input("Data limite (DD/MM/AAAA ou texto livre): ").strip()
        if not texto:
            return "Não definida"
        data = converter_data(texto)
        if data is not None and data < data_criacao:
            print("[ERRO] A data limite não pode ser anterior à data de criação "
                  f"({data_criacao.strftime('%d/%m/%Y')}).")
            continue
        return texto


# ----------------------------- Funcionalidades -----------------------------
def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def cadastrar_tarefa():
    print("\n--- Cadastro de nova tarefa ---")
    hoje = date.today()
    titulo = ler_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite(hoje)

    tarefas.append({
        "titulo": titulo,
        "descricao": descricao if descricao else "Sem descrição",
        "prioridade": prioridade,
        "data_criacao": hoje.strftime("%d/%m/%Y"),
        "data_limite": data_limite,
        "status": "Pendente",
    })
    print(f"\n[OK] Tarefa '{titulo}' cadastrada com sucesso!")


def visualizar_tarefas():
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return

    # Prioridade Alta aparece primeiro (sorted é estável: mantém ordem de cadastro).
    ordenadas = sorted(tarefas, key=lambda t: ORDEM_PRIORIDADE[t["prioridade"]])
    for i, t in enumerate(ordenadas, start=1):
        print(f"\nTarefa {i}")
        print(f"  Título       : {t['titulo']}")
        print(f"  Descrição    : {t['descricao']}")
        print(f"  Prioridade   : {t['prioridade']}")
        print(f"  Criada em    : {t['data_criacao']}")
        print(f"  Data limite  : {t['data_limite']}")
        print(f"  Status       : {t['status']}")
    print(f"\nTotal de tarefas: {len(ordenadas)}")


def main():
    print("Bem-vindo(a) ao TaskTracker!")
    try:
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
                print("[ERRO] Opção inválida. Escolha 1, 2 ou 3.")
    except (KeyboardInterrupt, EOFError):
        print("\nAplicação encerrada pelo usuário.")


if __name__ == "__main__":
    main()
