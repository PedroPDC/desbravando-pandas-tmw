# %%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
# Mostra uma série com os tipos de dados de cada coluna do dataframe
df.dtypes

# %%
# Convertendo Points para string
df["Points"].astype(str)

# %%
# Coluna auxiliar para exemplo
df["Points_double"] = df["Points"] * 2
df

# %%
# Convertendo mais de uma coluna de uma vez, para float
df[["Points", "Points_double"]].astype(float)

# %%
