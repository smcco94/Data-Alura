import pandas as pd

df = pd.read_csv('arquivos_aula/aluguel.csv', sep = ';')
# tipo = list(df.Tipo.drop_duplicates())
residencial = ['Quitinete', 'Casa','Apartamento','Casa de Condomínio','Casa de Vila']
selecao = df.Tipo.isin(residencial)
df_residencial = df[selecao]
df_residencial.index = range(df_residencial.shape[0])
df_residencial.columns.name = 'Id'
# df_residencial.sort_index(inplace = True, axis = 1)
#df_residencial.sort_values(inplace = True, by = ['Valor'])
# Exportando base de dados
#df_residencial.to_excel('arquivos_aula/df_residencial.xlsx', index = False)
df_residencial