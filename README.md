# TaskTracker

Sistema de gerenciamento de tarefas em linha de comando (CLI), desenvolvido em Python 3
como parte do **Bootcamp II – Fase 2 (Entrega Intermediária)**.

**Autora:** Gabriela Oliveira Bittencourt – Ciência da Computação (CEUB)

## Descrição funcional

Muitas pessoas perdem o controle de suas tarefas: esquecem prazos, não sabem o que já foi feito e
não enxergam o que é mais urgente. O TaskTracker resolve isso permitindo cadastrar e visualizar
tarefas de forma organizada, com prioridade e data limite.

### Funcionalidades

- **Cadastrar nova tarefa** com título, descrição, prioridade e data limite.
- **Visualizar tarefas cadastradas**, ordenadas por prioridade (Alta → Média → Baixa).
- **Sair** da aplicação.

### Regras de negócio

| Campo | Regra |
|-------|-------|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas e o prompt se repete. |
| Descrição | Texto livre. |
| Prioridade | Aceita somente `Alta`, `Média` (ou `Media`) e `Baixa` (sem diferenciar maiúsculas/minúsculas). Outros valores geram erro e repetição do prompt. |
| Data limite | Formato livre ou `DD/MM/AAAA`. Se informada em `DD/MM/AAAA`, deve ser válida e não pode ser anterior à data de criação. |
| Status | Definido automaticamente como `Pendente` no cadastro. |

> Os dados ficam apenas em memória durante a execução do programa.

## Tecnologias

- Python 3.8 ou superior (somente biblioteca padrão)
- Git e GitHub para versionamento

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf   # Planejamento lógico da Fase 1
└── src/
    └── main.py                   # Código-fonte da aplicação
```

## Instalação e execução

```bash
git clone https://github.com/SEU-USUARIO/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py        # no Linux/macOS, se necessário: python3 src/main.py
```

Não há dependências externas para instalar.

## Exemplo de uso

```
===== TASKTRACKER =====
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
Escolha uma opção: 1
Título da tarefa: 
[ERRO] O título é obrigatório e não pode ficar vazio.
```

## Próximos passos (Fase 3)

Empacotamento da aplicação, containerização com Docker, testes e deploy.
