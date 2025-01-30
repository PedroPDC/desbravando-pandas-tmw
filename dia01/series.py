# %%
import pandas as pd

# %%
idades = [30, 42, 90, 34]
idades

# %%
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) - 1)
variancia
# %%
# Transformação para séries Pandas
series_idades = pd.Series(idades)
series_idades

# %%
# Métodos da séries Pandas
# Média
series_idades.mean()

# %%
# Variância
series_idades.var()

# Desvio padrão
series_idades.std()

# %%
# Mediana
series_idades.median()

# %%
# 3° Quartil
series_idades.quantile(0.75)

# %%
# Sumarização
series_idades.describe()
# %%
# Dimensão da série
series_idades.shape

# %%
# Navegando na lista
idades[0]

# %%
# Navegando na série
series_idades[3]

# %%
# Alterando index da série
series_idades.index = ['p', 'e', 'd', 'r']
series_idades

# %%
# Navegando nos indices novos
series_idades['p']

# %%
series_idades[0]

# %%
series_idades.index = [40, 10, 30, 20]
series_idades

# %%
series_idades.iloc[2]

# %%
series_idades.iloc[2:3]

# %%
series_idades

# %%
series_idades.loc[40]

# %%
series_idades.name = 'idades'
series_idades

# %%
series_idades = pd.Series(idades, name="idades")
series_idades
# %%
