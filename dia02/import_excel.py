# IMPORTANDO DADOS DO EXCEL
# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%
# Shape do dataset
df.shape

# %%
# Primeiras 5 linhas do dataset
df.head()

# %%
# Ultimas 5 linhas do dataset
df.tail()

# %%
# Altera ordem das colunas
colunas = ["UUID", 
           "Points", 
           "IdCustomer", 
           "DtTransaction"]
df = df[colunas]
df

# %%
# Obtemos informações do tamanho do dataset 
df.info(memory_usage="deep")

# %%
