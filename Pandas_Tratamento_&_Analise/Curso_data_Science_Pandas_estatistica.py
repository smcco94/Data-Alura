from itertools import groupby
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("arquivos_aula/agrupar_residencial.csv", sep = ";")
df
grupo = df.groupby(df['Bairro'])
grupo[['Valor','Condominio','IPTU']].mean().round(2)
# Describe (dados relevantes para primeira analise inclusive detectar outliers)
grupo['Valor'].describe().round(2)
# Selecionando as estatisticas
grupo['Valor'].aggregate(['sum', 'min', 'max', 'std']).rename(columns={'sum': 'Soma', 'min': 'Mínimo', 'max': 'Máximo', 'std' : 'Desv Pad'})
plt.rc('figure', figsize = (20,40))
fig = grupo['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor médio do aluguel por bairro', {'fontsize':22})