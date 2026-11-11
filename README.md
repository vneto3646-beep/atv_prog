# Sistema de Gestão da Festa IFC Campus Blumenau

Este projeto é uma aplicação web desenvolvida com Streamlit para organizar a festa do IFC Campus Blumenau. O sistema permite controlar os alimentos que serão vendidos, os fornecedores que doam os insumos, as pessoas que irão atuar na festa e os preços de venda dos alimentos.

## Funcionalidades

- Cadastro, consulta, edição e remoção de alimentos;
- Cadastro, consulta, edição e remoção de fornecedores;
- Cadastro, consulta, edição e remoção de pessoas envolvidas;
- Cadastro, consulta, edição e remoção de preços de venda por alimento;
- Configuração do banco SQLite para testes locais;
- Configuração do banco MySQL para ambiente de produção;
- Uso de variáveis de ambiente para credenciais e conexão com MySQL.

## Tecnologias

- Python
- Streamlit
- SQLAlchemy
- SQLite
- MySQL
- uv

## Estrutura do projeto

```text
.
├── src/
│   ├── app.py
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   └── pages/
│       ├── 0_Inicio.py
│       ├── 1_Alimentos.py
│       ├── 2_Fornecedores.py
│       ├── 3_Pessoas.py
│       └── 4_Preços.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── data/
```

## Requisitos

- Python 3.11+
- uv

## Instalação

1. Clone o projeto e acesse a pasta raiz.
2. Instale as dependências com o uv:

```bash
uv sync
```

3. Crie um arquivo `.env` a partir do exemplo:

```bash
copy .env.example .env
```

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

4. Configure a variável `MYSQL_URL` no arquivo `.env` para uso em produção.

Exemplo:

```env
MYSQL_URL=mysql+pymysql://usuario:senha@host:3306/festa_ifc
```

Se o valor de `MYSQL_URL` não estiver definido, o sistema usa automaticamente o banco SQLite local na pasta `data/festival_local.db`.

## Execução

Para iniciar a aplicação:

```bash
uv run streamlit run src/app.py
```

A aplicação ficará disponível no navegador em `http://localhost:8501`.

## Banco de dados

- SQLite: usado para testes locais e desenvolvimento;
- MySQL: usado em produção e configurado por variável de ambiente.

## Observação

Os insumos da festa são tratados como doações, e os fornecedores representam as pessoas ou organizações que contribuem com esses materiais.
