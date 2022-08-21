import pandas as pd

df = pd.read_csv('arquivos_aula/aluguel.csv', sep = ';')
# Criando uma Series da coluna tipo a partir do dataframe
tipo = df.Tipo
# Inplace ja modifica a variavel, sem a necessidade de criar outra e incluir apos o drop
tipo.drop_duplicates(inplace = True)
tipo = pd.DataFrame(tipo)
# Corrigindo numercao index a partir da contagem dos itens
tipo.index = range(tipo.shape[0])
tipo.columns.name = 'Id'
tipo