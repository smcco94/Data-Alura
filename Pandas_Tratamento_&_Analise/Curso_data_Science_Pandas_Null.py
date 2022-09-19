import pandas as pd
#Chamando o dataframe
df = pd.read_excel('arquivos_aula/df_residencial.xlsx')
#Verificando a base para verificar valores nulos
df.info()
#Verificando 'Valor' Nulo
df[df['Valor'].isnull()]
#Retirando dados que possuem valor nulo
df.dropna(subset = ['Valor'], inplace = True)
#Verificando se 'Valor' Nulo foi eliminado
df[df['Valor'].isnull()]
#Verificando quantinhade de linhas da coluna condominio estao nulas
df[df['Condominio'].isnull()].shape[0]
#Selecao de dados nulos
selecao = (df['Tipo'] == 'Apartamento') & (df['Condominio'].isnull())
#com a selecao de apartametno com condominio sem valor eu agrego um novo valor para df somente 
# com os que nao possuem valor nulo, invertendo a selecao com o sinal de ~
df = df[~selecao]
# Alternar valores vazios para zero e aplicar a alteracao com a funcao inplace
#df.fillna(0, inplace = True)
# Outro jeito seria criar um dicionario e indicar a coluna e o valor a ser substituido para cada uma
df = df.fillna({'Condominio': 0, 'IPTU': 0})
# Verifico novamento o tipo da tabela, e salvo em um csv os novos dados
df.info()
df.to_csv('arquivos_aula/aluguel_residencial.csv', sep = ';', index = False)