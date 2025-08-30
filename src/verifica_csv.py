import pandas as pd

caminho = "data/desafio_indicium_imdb.csv"
df = pd.read_csv(caminho)

print("Primeiras linhas do CSV:")
print(df.head())

print("Informações das colunas:")
print(df.info())

print("Valores ausentes por coluna:")
print(df.isnull().sum())