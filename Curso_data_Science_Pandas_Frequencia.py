from tkinter import N
import pandas as pd

df = pd.read_csv('arquivos_aula/aluguel_residencial.csv', sep = ';')

#Selecione somente os imóveis classificados com tipo 'Apartamento'.
selecao = df['Tipo'] == 'Apartamento'
n1 = df[selecao].shape[0]

#Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
selecao2 = (df['Tipo'] == 'Casa') | (df['Tipo'] == 'Casa Condomínio') | (df['Tipo'] == 'Casa de Vila')
n2 = df[selecao2].shape[0]

#Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
selecao3 = (df['Area'] >= 60) & (df['Area'] <= 100)
n3 = df[selecao3].shape[0]

#Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
selecao4 = (df['Quartos'] >= 4) & (df['Valor'] < 2000)
n4 = df[selecao4].shape[0]

print(f"Quantidade Apartamentos: {n1}")
print(f"Quantidade Casa, Casa de Vila e Casa Condomínio: {n2}")
print(f"Quantidade entre 60 e 100 m2: {n3}")
print(f"Quantidade 4 quartos ou mais com valor abaixo de 2000: {n4}")