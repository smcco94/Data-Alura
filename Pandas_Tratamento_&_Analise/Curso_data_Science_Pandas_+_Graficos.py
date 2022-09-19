from random import sample
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,9))
df = pd.read_csv('arquivos_aula/aluguel_residencial_sem_outliers.csv', sep = ';')
df.head(10)
area = plt.figure()
g1 = area.add_subplot(2,2,1)
g2 = area.add_subplot(2,2,2)
g3 = area.add_subplot(2,2,3)
g4 = area.add_subplot(2,2,4)

g1.scatter(df['Valor'], df['Area'])
g1.set_title('Valor x Area')

g2.hist(df['Valor'])
g2.set_title('Histograma')

dados_g3 = df['Valor'].sample(100)
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra Valor')

grupo = df.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values
g4.bar(label, valores)
g4.set_title('Valor Médio por tipo')

area.savefig('Graficos.png', dpi = 300, bbox_inches = 'tight')