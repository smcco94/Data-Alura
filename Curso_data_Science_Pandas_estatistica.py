from itertools import groupby
import pandas as pd
df = pd.read_csv("arquivos_aula/agrupar_residencial.csv", sep = ";")
df
grupo = df.groupby(df['Bairro'])
grupo[['Valor','Condominio','IPTU']].mean().round(2)