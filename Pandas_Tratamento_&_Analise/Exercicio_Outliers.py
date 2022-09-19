import pandas as pd
import matplotlib.pyplot as plt

from Curso_data_Science_Pandas_Outliers import Q1
plt.rc('figure', figsize = (14,6))
df = pd.read_csv('arquivos_aula/aluguel_amostra.csv', sep = ';')
Valor_m2 = df['Valor m2'].round(2)
plt.boxplot(Valor_m2)
Q1 = Valor_m2.quantile(.25)
Q3 = Valor_m2.quantile(.75)
IQQ = Q3 - Q1
lim_inf = Q1 - 1.5 * IQQ
lim_sup = Q1 + 1.5 * IQQ