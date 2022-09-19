import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,9))
df = pd.read_csv('arquivos_aula/aluguel_residencial.csv', sep = ';')
grupo_tipo = df.groupby('Tipo')['Valor']
Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inf = Q1 - 1.5 * IIQ
limite_sup = Q3 + 1.5 * IIQ
df_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    e_tipo = df['Tipo'] == tipo
    e_dentro_lim = (df['Valor'] >= limite_inf[tipo]) & (df['Valor'] <= limite_sup[tipo])
    selecao = e_tipo & e_dentro_lim
    dado_selecao = df[selecao]
    df_new = pd.concat([df_new, dado_selecao])
df_new.boxplot(['Valor'], by = ['Tipo'])
df_new.to_csv('arquivos_aula/aluguel_residencial_sem_outliers.csv', sep = ';', index=False)