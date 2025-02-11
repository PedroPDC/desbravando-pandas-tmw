# %%
import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers

# %%
# Retorna uma tupla com o numero de linhas e colunas
df_customers.shape

# %%
# Verificando quanto o dataset está ocupando em memoria
df_customers.info(memory_usage="deep")

# %%
# Estatistica descritiva do dataset
df_customers["Points"].describe()

# %%
condicao = df_customers["Points"] > 1000

df_customers[condicao]

# %%
# Podemos utilizar assim
maximo = df_customers["Points"].max()
condicao = df_customers["Points"] == maximo

df_customers[condicao]

# %%
# Como tambem podemos utilizar assim
condicao = df_customers["Points"] == df_customers["Points"].max()

df_customers[condicao]

# %%
# Forma mais comum
df_customers[df_customers["Points"] == df_customers["Points"].max()]

# %%
# Obtendo o nome do usuario com mais pontos
df_customers[df_customers["Points"] == df_customers["Points"].max()]["Name"].iloc[0]

# %%
# Melhorando visualização do código
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]

# %%
# Filtro para pegar quem tem entre 1000 e 2000 pontos

condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000) 
df_customers[condicao]

# %%

a = [1, 2, 3, 4]
b = a.copy()
print(a)
print(b)

b.append(5)
print(a)
print(b)

# %%
df_customers

# %%
df_customers[["UUID", "Name"]]
# %%
colunas = df_customers.columns.tolist()
colunas.sort()

df_customers = df_customers[colunas]
df_customers
# %%
# O rename cria um dataframe NOVO
df_customers = df_customers.rename(columns={"Name": "Nome", 
                            "Points": "Pontos"})
df_customers
# %%
# Forma de renomear coluna de forma direta, sem necessidade de reatribuição
df_customers.rename(columns={"UUID": "Id"}, inplace=True)
df_customers
# %%
