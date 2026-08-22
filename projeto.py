import pandas as pd
import numpy as np
import unicodedata
import mysql.connector 

## Função para normalizar texto
def normalizar_texto(valor):

    if pd.isna(valor):
        return valor

    valor = str(valor).strip().lower()

    valor = unicodedata.normalize("NFKD", valor)

    valor = "".join(
        c for c in valor
        if not unicodedata.combining(c)
    )

    return valor

#Criando um mapa de idiomas para padronizar os valores da coluna idioma, pois tem valores diferentes que significam o mesmo idioma, como "ingles" e "english"
mapa_idiomas = {
    "ingles": "Inglês",
    "english": "Inglês",
    "en": "Inglês",

    "espanhol": "Espanhol",
    "espanol": "Espanhol",
    "spanish": "Espanhol",
    "es": "Espanhol",

    "alemao": "Alemão",
    "german": "Alemão",
    "de": "Alemão",

    "mandarim": "Mandarim",
    "chinese": "Mandarim",
    "chines": "Mandarim",
    "zh": "Mandarim",

    "italiano": "Italiano",
    "italian": "Italiano",
    "it": "Italiano",

    "japones": "Japonês",
    "japanese": "Japonês",
    "ja": "Japonês",

    "sueco": "Sueco",
    "swedish": "Sueco",
    "sv": "Sueco",

    "portugues": "Português",
    "portuguese": "Português",
    "pt-br": "Português",

    "dinamarques": "Dinamarquês",
    "danish": "Dinamarquês",
    "da": "Dinamarquês",

    "coreano": "Coreano",
    "korean": "Coreano",
    "ko": "Coreano",

    "frances": "Francês",
    "french": "Francês",
    "fr": "Francês",

    "hindi": "Hindi",
    "hi": "Hindi"
}

#Criando mapa de paises para padronizar os valores da coluna pais, pois tem valores diferentes que significam o mesmo país, como "estados unidos" e "usa"
mapa_paises = {
    "estados unidos": "Estados Unidos",
    "usa": "Estados Unidos",
    "eua": "Estados Unidos",

    "reino unido": "Reino Unido",
    "uk": "Reino Unido",
    "united kingdom": "Reino Unido",

    "itália": "Itália",
    "italia": "Itália",
    "italy": "Itália",

    "japão": "Japão",
    "japao": "Japão",
    "japan": "Japão",

    "nova zelândia": "Nova Zelândia",
    "nova zelandia": "Nova Zelândia",
    "new zealand": "Nova Zelândia",

    "méxico": "México",
    "mexico": "México",

    "brasil": "Brasil",
    "brazil": "Brasil",

    "canadá": "Canadá",
    "canada": "Canadá",

    "alemanha": "Alemanha",
    "germany": "Alemanha",

    "suécia": "Suécia",
    "suecia": "Suécia",
    "sweden": "Suécia",

    "china": "China",

    "coreia do sul": "Coreia do Sul",
    "coréia do sul": "Coreia do Sul",
    "south korea": "Coreia do Sul",

    "dinamarca": "Dinamarca",
    "denmark": "Dinamarca",

    "austrália": "Austrália",
    "australia": "Austrália",

    "áustria": "Áustria",
    "austria": "Áustria",

    "espanha": "Espanha",
    "spain": "Espanha",

    "taiwan": "Taiwan",

    "argentina": "Argentina",

    "frança": "França",
    "franca": "França",
    "france": "França",

    "índia": "Índia"
}





#Lendo arquivo, aba filmes
dataFilmes = pd.read_excel('./dados/dados brutos.xlsx', sheet_name='Filmes')

## TRATANDO ABA FILMES__________________________________________________________________________________________________________________________________________________
#Encontrando valores nulos na aba Filmes
#valores_nulos = dataFilmes.isnull().sum()
#print(valores_nulos)

#Excluindo linhas com valores nulos na coluna 'Titulo', não tem sentido ter valores nulos nessa coluna, pois é o nome do filme
dataFilmes.dropna(subset=['titulo'], inplace=True)

#Preenchendo valores nulos na coluna 'diretor' com "Não Informado"
#Pega a coluna -> trate os nulos -> devolva a coluna tratada para a coluna original
dataFilmes["diretor"] = dataFilmes["diretor"].fillna("Não Informado")


#Padronizando a coluna data de lancamento, se retornar Nat, significa que teem datas que não existem, como 31/02/2020
dataFilmes['data_lancamento'] = pd.to_datetime(dataFilmes['data_lancamento'], format='mixed' ,dayfirst=True, errors='coerce')




#padronizndo coluna duracao minutos pegando só os números da coluna, pois tem valores que estão com texto junto, como "120 minutos"
dataFilmes['duracao_minutos'] = (dataFilmes["duracao_minutos"].astype(str).str.extract(r"(\d+(?:[.,]\d+)?)")[0])
#transformando coluna em numerica
dataFilmes['duracao_minutos'] = pd.to_numeric(dataFilmes['duracao_minutos'], errors='coerce')



#Padronizando coluna Nota, trocando virgula por ponto
dataFilmes['nota'] = pd.to_numeric(dataFilmes['nota'].astype(str).str.replace(',', '.', regex=False))
#convertendo pra número
dataFilmes['nota'] = pd.to_numeric(dataFilmes['nota'], errors='coerce')
#Transformando notas negativas em nulas
dataFilmes.loc[dataFilmes['nota'] < 0, 'nota'] = np.nan


#Padronizando coluna quantidade de avaliações
dataFilmes['quantidade_avaliacoes'] = pd.to_numeric(dataFilmes['quantidade_avaliacoes'], errors='coerce')
# Tratando valores imensos e transforamdo em nulos, pois o tipo de dado da coluna no banco de dados é INT, e o valor máximo que um INT pode ter é 2147483647
dataFilmes.loc[dataFilmes['quantidade_avaliacoes'] > 2147483647,'quantidade_avaliacoes'] = np.nan



#Padronizando coluna orçamento, removendo letras e pontuações
dataFilmes["orcamento"] = (dataFilmes["orcamento"].astype(str).str.replace("US$", "", regex=False).str.replace(".", "", regex=False).str.strip())
#Convertendo para número
dataFilmes["orcamento"] = pd.to_numeric(dataFilmes["orcamento"], errors='coerce')
#tratando valores negativos, transformando em nulos
dataFilmes.loc[dataFilmes["orcamento"] < 0, "orcamento"] = np.nan


#Padronizando coluna receita, igual a coluna orçamento
dataFilmes["receita"] = (dataFilmes["receita"].astype(str).str.replace("US$", "", regex=False).str.replace(".", "", regex=False).str.strip())
#Convertendo para número
dataFilmes["receita"] = pd.to_numeric(dataFilmes["receita"], errors='coerce')
#tratando valores negativos, transformando em nulos
dataFilmes.loc[dataFilmes["receita"] < 0, "receita"] = np.nan

#Padronizando coluna idioma
dataFilmes["idioma"] = dataFilmes["idioma"].apply(normalizar_texto)
dataFilmes["idioma"] = dataFilmes["idioma"].replace(mapa_idiomas)

#Padronizando coluna diretor, deixando tudo minusculo e depois colocando a primeira letra de cada palavra em maiúsculo
dataFilmes["diretor"] = dataFilmes["diretor"].str.lower().str.title()

#Padronizando coluna pais, deixando tudo minusculo e tirando acentos
dataFilmes["pais"] = dataFilmes["pais"].str.strip().str.lower()
dataFilmes["pais"] = dataFilmes["pais"].replace(mapa_paises)

#removendo colunas que não serão utilizadas no banco de dados, pois não tem relação com as outras tabelas
dataFilmes = dataFilmes.drop(columns=["diretor", "pais"])
#renomeando para deixar igual a tabela no banco de dados, para poder fazer o relacionamento entre as tabelas
dataFilmes.rename(columns={"diretor_id": "id_diretor"}, inplace=True)

#transformando valores NaN em None, para poder inserir no banco de dados
dataFilmes = dataFilmes.astype(object).where(pd.notna(dataFilmes), None)



#TRATANDO ABA GENEROS__________________________________________________________________________________________________________________________________________________________

dataGenero = pd.read_excel('./dados/dados brutos.xlsx', sheet_name='Generos')

#colocando a primeria linha da palavra em maiusculo
dataGenero["genero"] = dataGenero["genero"].str.lower().str.title()
#inserindo um valor dentro de uma celula que esta vazia
dataGenero.loc[dataGenero["id_genero"] == 8, "descricao"] = "Filmes voltados para toda a família."
dataGenero.loc[dataGenero["id_genero"] == 5, "descricao"] = "Filmes onde há investigação de crimes, geralmente com detetives ou policiais como protagonistas."
dataGenero.loc[dataGenero["id_genero"] == 12, "descricao"] = "Filmes que exploram o desconhecido, o sobrenatural ou o inexplicável, muitas vezes envolvendo suspense e medo."

#TRATANDO A ABA DIRETORES__________________________________________________________________________________________________________________________________________________________

dataDiretores = pd.read_excel('./dados/dados brutos.xlsx', sheet_name='Diretores')

#colocando a primeira letra da palavra em maiusculo
dataDiretores["nome"] = dataDiretores["nome"].str.lower().str.title()
dataDiretores["nacionalidade"] = dataDiretores["nacionalidade"].str.strip().str.lower()

#Preenchendo nulos na coluna nacionalidade com "Não informado"
dataDiretores["nacionalidade"] = dataDiretores["nacionalidade"].fillna("Não informado")

#Padronizando a coluna data de nascimento, se retornar Nat, significa que tem datas que não existem, como 31/02/2020
dataDiretores["data_nascimento"] = pd.to_datetime(dataDiretores["data_nascimento"], format='mixed', dayfirst=True, errors='coerce')

#TRATANDO A ABA PAISES__________________________________________________________________________________________________________________________________________________________

dataPaises = pd.read_excel('./dados/dados brutos.xlsx', sheet_name='Paises')

#colocando a primeira letra da palavra em maiusculo
dataPaises["pais"] = dataPaises["pais"].str.lower().str.title()
dataPaises["continente"] = dataPaises["continente"].str.lower().str.title()


#Salvando as planilhas tratadas em um novo arquivo Excel

with pd.ExcelWriter('./dados/dados tratados.xlsx') as writer:
    dataFilmes.to_excel(writer, sheet_name='Filmes', index=False)
    dataGenero.to_excel(writer, sheet_name='Generos', index=False)
    dataDiretores.to_excel(writer, sheet_name='Diretores', index=False)
    dataPaises.to_excel(writer, sheet_name='Paises', index=False)


#INSERINDO OS DADOS DENTRO DAS TABELAS NO MYSQL______________________________________________________________________________________________________________________________

# conexao = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Matrix200@",
#     database="etl_filmes"
# )

# cursor = conexao.cursor()

# sql = """
#     INSERT INTO Paises (id_pais, pais, continente)
#     VALUES (%s, %s, %s)
# """

# for _, linha in dataPaises.iterrows():
#     cursor.execute(sql, (
#                         linha['id_pais'], 
#                          linha['pais'], 
#                          linha['continente']
#                          )
#                     )


# conexao.commit()

# sql_diretores = """
# INSERT INTO Diretores (
#     id_diretor,
#     nome,
#     nacionalidade,
#     data_nascimento
# )
# VALUES (%s, %s, %s, %s)
# """

# for _, linha in dataDiretores.iterrows():
#     cursor.execute(sql_diretores, (
#         linha["id_diretor"],
#         linha["nome"],
#         linha["nacionalidade"],
#         linha["data_nascimento"]
#     ))

# conexao.commit()


# sql_generos = """
# INSERT INTO Generos (
#     id_genero,
#     genero,
#     descricao
# )
# VALUES (%s, %s, %s)
# """

# for _, linha in dataGenero.iterrows():
#     cursor.execute(sql_generos, (
#         linha["id_genero"],
#         linha["genero"],
#         linha["descricao"]
#     ))

# conexao.commit()




# sql_filmes = """
# INSERT INTO Filmes (
#     id_filme,
#     titulo,
#     data_lancamento,
#     duracao_minutos,
#     nota,
#     quantidade_avaliacoes,
#     orcamento,
#     receita,
#     idioma,
#     id_diretor,
#     pais_id
# )
# VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# """

# for _, linha in dataFilmes.iterrows():
#     cursor.execute(sql_filmes, (
#         linha["id_filme"],
#         linha["titulo"],
#         linha["data_lancamento"],
#         linha["duracao_minutos"],
#         linha["nota"],
#         linha["quantidade_avaliacoes"],
#         linha["orcamento"],
#         linha["receita"],
#         linha["idioma"],
#         linha["id_diretor"],
#         linha["pais_id"]
#     ))

# conexao.commit()


