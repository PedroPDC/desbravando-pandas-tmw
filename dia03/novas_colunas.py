# %%

import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/customers.csv", sep=";")

# %%
# Criando uma coluna nova a partir de uma existente
df["Points_double"] = df["Points"] * 2
df

# %%
# Retorna uma série nova
df["Points_ratio"] = df["Points_double"] / df["Points"]
df

# %%
# Criando coluna a partir de um escalar
df["Constante"] = None
df

# %%

# Utilizando biblioteca numpy para obtermos logaritmo da coluna Points
df["Points_log"] = np.log(df["Points"])
df

# %%
# Outro teste
np.log(df[["Points", "Points_double", "Points_ratio"]])

# %%

# Colocando coluna em caixa alta (FORMA "LEGADO", nao recomendável)
nomes_alta = []

for i in df["Name"]:
    nomes_alta.append(i.upper())

df["Nome_Alta"] = nomes_alta
df

# %%
# Colocando coluna em caixa alta usando pandas
df["Name"].str.upper()

# %%
# Função para obter o primeiro nome dos usuarios (para o caso em que usuarios tenham _ no nome)
def get_first(nome:str):
    return nome.split("_")[0]

# %% 
# Aplicando uma função a todas as linhas da série
df["Name_First"] = df["Name"].apply(get_first)
df


# %%
# Usando funcoes lambda
soma = lambda x,y: x + y

# %%
# Adaptando a funcao criada anteriormente, ficaria assim:
get_f = lambda nome: nome.split("_")[0]
get_f("Pedro_Paulo")

# %%
# Usando lambda no APPLY
df["Name"].apply( lambda x: x.upper().split("_")[0] )
# %%

# Definindo intervalo de pontos
def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "medio"
    else:
        return "alto"
    
df["Faixa_Pontos"] = df["Points"].apply(intervalo_pontos)
df

# %%

# Pegando 3 ultimos digitos da UUID
df["UUID"].apply(lambda x: x[-3:])

# %%
df

# %% 
# Fazendo um apply em um DATAFRAME

data = {
    "Nome": ["Téo", "Nah", "Maria", "Lara"],
    "Recencia": [1, 30, 10, 45],
    "Valor": [100, 2000, 15, 500],
    "Frequencia": [2, 5, 1, 15]
}

df_crm = pd.DataFrame(data)
df_crm

# Criaremos uma nota para cada usuario que será uma combinação de Recencia, Valor e Frequencia
# Essa funcao recebe uma linha do DataFrame, que é uma série, vamos pegar os indices dela e aplicar a funcao
# Recebemos a linha inteira como se fosse uma série e posteriormente faremos o apply linha a linha (já que o apply aceita apenas valores que sao series)
def rfv(row):
    nota = 0

    if row["Recencia"] <= 10:
        nota += 10
    elif 10 < row["Recencia"] <= 30:
        nota += 5
    elif row["Recencia"] > 30:
        nota += 0
    
    if row["Valor"] > 1000:
        nota += 10
    elif 100 <= row["Valor"] < 1000:
        nota += 5
    elif row["Valor"] < 100:
        nota += 0
    
    if row["Frequencia"] > 10:
        nota += 10
    elif 5 <= row["Frequencia"] < 10:
        nota += 5
    elif row["Frequencia"] < 5:
        nota += 0
    
    return nota

# %%
df_crm["RFV"] = df_crm.apply(rfv, axis=1)
df_crm

# %%
