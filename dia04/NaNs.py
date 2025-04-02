# %%
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31, 32, 34, 12, np.nan],
    "renda":[np.nan, 3245, 357, 12432, np.nan]
}

df = pd.DataFrame(data)
df
# %%

# Para sabermos a qtde de nulos
df["idade"].isna().sum()

# %%

# Para sabermos a qtde de nulos COLUNA POR COLUNA
df.isna().sum()

# %%

# Taxa de valores nulos por coluna
df.isna().mean()

# %%

# Preenchendo nulos com a média de cada coluna
df.fillna({
    "idade": df["idade"].mean(),
    "renda": df["renda"].mean()
})

# %%

df.dropna(subset=["idade", "renda"] ,how='all')

# %%

df.dropna(axis=1, how='all')

# %%
