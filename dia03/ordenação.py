# %%
import pandas as pd

# %%
df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%
# Adicionando critério de "desempate"
df.sort_values(by=["Points", "Name"], ascending=[False, True])

# %%
# Funções encadeadas
df = (df.sort_values(by=["Points", "Name"], 
                     ascending=[False, True])
        .rename(columns={"Name": "Nome", "Points": "Pontos"}))
df
# %%
