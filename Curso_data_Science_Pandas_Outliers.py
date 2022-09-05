import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))
df = pd.read_csv('arquivos_aula/aluguel_residencial.csv', sep = ';')
valor = df['Valor']
Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inf = Q1 - 1.5 * IIQ
limite_sup = Q3 + 1.5 * IIQ
selecao = (valor >= limite_inf) & (valor <= limite_sup)
df_new = df[selecao]
df_new.boxplot(['Valor'])
df.hist(['Valor'])
df_new.hist(['Valor'])