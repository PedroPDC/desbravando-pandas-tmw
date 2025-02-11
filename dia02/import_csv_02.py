# Neste arquivo importaremos outro dataset
# %%
import pandas as pd

df = pd.read_csv("../data/products.csv", 
                 sep=";",
                 names=["Id", "Name", "Description"]
                 )

df

# %%
# Exercicio Proposto: Renomear as colunas traduzindo para o português

df.rename(columns={"Name": "Nome", 
                   "Description": "Descrição"}, 
                   inplace=True)
df
# %%
