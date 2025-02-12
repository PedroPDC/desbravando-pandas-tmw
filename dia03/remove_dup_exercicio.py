# %%

import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
# %%

# Exercicio Proposto - Para cada um dos IdCustomer, queremos saber a DtTransaction, UUID e os Pontos
df_last = (df.sort_values(by="DtTransaction", ascending=False)
        .drop_duplicates(subset=["IdCustomer"], keep="first"))

# Verifica valores unicos de uma coluna
df_last["IdCustomer"].nunique()
# %%

# Faz uma busca no dataframe ORIGINAL pelo IdCustomer desejado
condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df[condicao]

# %%

# Busca o mesmo usuario no dataframe que as duplicadas foram removidas, 
# para verificar se horario coincide com o mesmo do ultimo registro do dataset original
df_last[df_last["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"]
# %%
