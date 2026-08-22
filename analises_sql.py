import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


# ============================================================
# CONEXÃO COM O MYSQL
# ============================================================

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Matrix200@",
    database="etl_filmes"
)



# ============================================================
# ANÁLISE: FILMES POR PAÍS
# GRÁFICO: BARRAS
# ============================================================

query = """
SELECT
    p.pais,
    COUNT(f.id_filme) AS quantidade_filmes
FROM Filmes f
INNER JOIN Paises p
    ON f.pais_id = p.id_pais
GROUP BY p.id_pais, p.pais
ORDER BY quantidade_filmes DESC
LIMIT 10;
"""

df_filmes_pais = pd.read_sql(query, conexao)

print("\n--- Top 10 países por quantidade de filmes ---")
print(df_filmes_pais)

plt.figure(figsize=(10, 6))

plt.bar(
    df_filmes_pais["pais"],
    df_filmes_pais["quantidade_filmes"]
)

plt.title("Top 10 Países por Quantidade de Filmes")
plt.xlabel("País")
plt.ylabel("Quantidade de filmes")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()


# ============================================================
# ANÁLISE: RECEITA POR IDIOMA
# GRÁFICO: PIZZA
# ============================================================

query = """
SELECT
    idioma,
    SUM(receita) AS receita_total
FROM Filmes
WHERE receita IS NOT NULL
AND idioma IS NOT NULL
GROUP BY idioma
ORDER BY receita_total DESC;
"""

df_receita_idioma = pd.read_sql(query, conexao)

# Para não gerar uma pizza com muitos pedaços,
# pegamos os 5 maiores e agrupamos o restante como "Outros"

top_5 = df_receita_idioma.head(5).copy()

receita_outros = df_receita_idioma.iloc[5:]["receita_total"].sum()

if receita_outros > 0:
    outros = pd.DataFrame({
        "idioma": ["Outros"],
        "receita_total": [receita_outros]
    })

    df_pizza = pd.concat(
        [top_5, outros],
        ignore_index=True
    )
else:
    df_pizza = top_5


plt.figure(figsize=(8, 8))

plt.pie(
    df_pizza["receita_total"],
    labels=df_pizza["idioma"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Participação da Receita por Idioma")

plt.tight_layout()
plt.show()

# ============================================================ 
#  PRIMEIRA ANÁLISE: RECEITA POR ANO 
#  GRÁFICO: LINHA 
#  ==========================================================
query = """
SELECT YEAR(data_lancamento) AS ano, SUM(receita) AS receita_total 
FROM Filmes 
WHERE data_lancamento IS NOT NULL 
AND receita IS NOT NULL
GROUP BY YEAR(data_lancamento) 
ORDER BY ano; 
""" 

df_receita_ano = pd.read_sql(query, conexao) 

print("\n--- Receita por ano ---") 
print(df_receita_ano) 

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df_receita_ano["ano"], df_receita_ano["receita_total"], marker="o")
ax.set_title("Evolução da Receita por Ano")
ax.set_xlabel("Ano")
ax.set_ylabel("Receita")

ax.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f'US$ {x/1e6:,.0f}M')
)

ax.grid(True)
plt.tight_layout()
plt.show()



# ============================================================
# FECHANDO A CONEXÃO
# ============================================================

conexao.close()

print("\nAnálises concluídas!")

