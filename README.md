# 🔄 Projeto ETL — Tratamento e Integração de Dados

Projeto prático desenvolvido para simular um processo de **ETL (Extract, Transform, Load)**, utilizando Python e Pandas para tratamento e transformação de dados, seguido da integração com banco de dados SQL.

O projeto foi desenvolvido com o objetivo de trabalhar conceitos de **qualidade de dados, limpeza, padronização, transformação e armazenamento**, simulando um cenário próximo ao encontrado em processos reais de dados.

---

## 🎯 Objetivo

Construir um fluxo de ETL capaz de transformar uma base de dados inicialmente desorganizada em uma estrutura **limpa, padronizada e pronta para utilização em um banco de dados**.

O projeto contempla as seguintes etapas:

`📥 Extração → 🧹 Tratamento → 🔄 Transformação → 🗄️ Carga → 🔎 Consulta`

---

## 🗂️ Etapas do Projeto

### 📥 1. Extração

Os dados foram disponibilizados inicialmente em arquivos contendo informações propositalmente inconsistentes, simulando problemas comuns encontrados em bases reais.

Através do Python e Pandas, os arquivos foram carregados para DataFrames para iniciar o processo de tratamento.

---

### 🧹 2. Tratamento e Limpeza

Durante essa etapa foram identificados e corrigidos diferentes problemas de qualidade dos dados.

**Principais tratamentos realizados:**

* 🔤 Padronização de textos
* ✍️ Correção de nomes inconsistentes
* 🧹 Tratamento de valores ausentes
* 🔁 Identificação e tratamento de duplicidades
* 📅 Padronização de datas
* 🔢 Correção de tipos de dados
* 📐 Padronização de formatos
* ✅ Validação dos dados após o tratamento

Exemplo de inconsistência encontrada:

```text
Peter Jackson
peter jackson
Peter jackson
PETER JACKSON
```

Após o processo de tratamento, os registros foram padronizados para uma única representação:

```text
Peter Jackson
```

---

### 🔄 3. Transformação

Após a limpeza, os dados foram transformados e organizados utilizando **Pandas**, preparando as informações para serem armazenadas e posteriormente consultadas.

Foram utilizadas operações de:

* Seleção e renomeação de colunas
* Transformação de valores
* Filtragem de registros
* Criação de novas informações
* Padronização de categorias
* Organização dos DataFrames

---

### 🗄️ 4. Carga no Banco de Dados

Após o tratamento, os dados foram preparados para serem armazenados em um banco de dados SQL.

A integração foi realizada utilizando **Python**, permitindo que os dados tratados fossem enviados para o banco e posteriormente consultados através de SQL.

---

### 🔎 5. Consultas SQL

Com os dados carregados, foram realizadas consultas para validar as informações e explorar os dados tratados.

Essa etapa permitiu verificar se o processo de ETL produziu uma base consistente e adequada para consultas e análises.

---

## 🏗️ Fluxo do ETL

```text
┌─────────────────┐
│   📁 Dados      │
│     Brutos      │
└────────┬────────┘
         ↓
┌─────────────────┐
│  🐍 Python +    │
│    🐼 Pandas    │
└────────┬────────┘
         ↓
┌─────────────────┐
│   🧹 Limpeza    │
│  e Padronização │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 🔄 Transformação│
│   dos Dados     │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 🗄️ Banco SQL    │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 🔎 Consultas e  │
│    Validação    │
└─────────────────┘
```

---

## 🛠️ Tecnologias e Ferramentas

<p align="left">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40"/>

</p>

### 🐍 Linguagem

* Python

### 🐼 Manipulação de Dados

* Pandas
* DataFrames
* Tratamento e transformação de dados

### 🗄️ Banco de Dados

* SQL
* MySQL

---

## 📂 Estrutura do Projeto

```text
ETL-Python-SQL/
│
├── 📁 dados/
│   ├── dados_brutos/
│   └── dados_tratados/
│
├── analises_sql.py
│
├── projeto.py
│
└── README.md
```

---

## 📚 Aprendizados

Este projeto permitiu colocar em prática conceitos importantes relacionados à área de Dados, principalmente:

* 🧹 Limpeza e qualidade de dados
* 🐍 Manipulação de dados com Python
* 🐼 Utilização da biblioteca Pandas
* 🔄 Construção de um fluxo ETL
* 🗄️ Integração entre Python e SQL
* 🔎 Consultas e validação de dados
* 📊 Organização de dados para análises futuras


🔗 [LinkedIn](https://www.linkedin.com/in/renanvtimozzi/)

🔗 [GitHub](https://github.com/renanvicentee)
