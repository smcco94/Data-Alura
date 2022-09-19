import pandas as pd
df = pd.read_csv('arquivos_aula/aluguel.csv', sep = ';')
df.head(10)
classes = [0,2,4,6,100]
labels = ['0 a 2 quartos', '3 a 4 quartos', '5 e 6 quartos', '7 quartos ou mais']
quartos = pd.cut(df.Quartos, classes, labels = labels, include_lowest= True)
pd.value_counts(quartos)