# TaskTracker

Sistema de gerenciamento de tarefas em linha de comando (CLI), desenvolvido em Python 3
como parte do **Bootcamp II** (Fase 2 – Desenvolvimento e Fase 3 – Conteinerização com Docker).

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
| Prioridade | Aceita somente `Alta`, `Média` (ou `Media`) e `Baixa` (sem diferenciar maiúsculas/minúsculas). |
| Data limite | Formato livre ou `DD/MM/AAAA`. Se informada em `DD/MM/AAAA`, não pode ser anterior à data de criação. |
| Status | Definido automaticamente como `Pendente` no cadastro. |

> Os dados ficam apenas em memória durante a execução do programa.

## Tecnologias

- Python 3.11 (somente biblioteca padrão)
- Docker e Docker Compose
- Git e GitHub

## Estrutura do repositório

```
tasktracker-projeto/
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf   # Planejamento lógico da Fase 1
├── src/
│   └── main.py                   # Código-fonte da aplicação
├── Dockerfile                    # Receita da imagem Docker
├── docker-compose.yml            # Orquestração da execução interativa
└── README.md
```

## Guia Docker

**Pré-requisito:** Docker Desktop (ou Docker Engine) instalado e em execução.

```bash
git clone https://github.com/gabi-bitt/tasktracker-projeto.git
cd tasktracker-projeto
```

### Como construir a imagem

```bash
docker build -t tasktracker-app .
```

### Como rodar o container em modo isolado

```bash
docker run -it --rm tasktracker-app
```

As flags `-it` são obrigatórias: a aplicação usa `input()` e precisa de um terminal interativo.

### Como rodar via orquestração (Recomendado)

```bash
docker compose run --rm tasktracker
```

O `docker-compose.yml` define `stdin_open: true` (mantém a entrada de dados aberta) e `tty: true`
(aloca um terminal virtual), o que permite usar o menu da CLI dentro do container.

## Execução sem Docker (opcional)

```bash
python src/main.py
```

## Dockerfile em resumo

| Instrução | Função |
|-----------|--------|
| `FROM python:3.11-slim` | Base leve do sistema com Python |
| `WORKDIR /app` | Pasta de trabalho no container |
| `ENV PYTHONUNBUFFERED=1` | Saída imediata de logs/prints |
| `COPY src/ /app/src/` | Injeta o código-fonte na imagem |
| `CMD ["python", "src/main.py"]` | Dispara a aplicação |
