# 2 Converta o seguinte dicionário para DataFrame e obtenha:
# Sumário de cada coluna
# Média da coluna idade
# Último nome da coluna nome

# dados = {“nome”:[“Téo”, “Nah”, “Napoleão”], “idade”: [31, 32, 14]}

import pandas as pd

dados = {
    "nome": ["Téo", "Nah", "Napoleão"],
    "idade": [31, 32, 14]
}

df = pd.DataFrame(dados)

print(df["nome"].describe())
print(f"\n\nMédia de idades: {df["idade"].mean()}")
print(f"Último nome: {df["nome"].iloc[-1]}")

# print(df["nome"].tail(1)) tambem funcionaria no ultimo nome