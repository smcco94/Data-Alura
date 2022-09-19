# Chamando bibliotecas
import pandas as pd
# Lendo arquivo cs e exibindo 10 primeiras linhas CSV
df = pd.read_csv('arquivos_aula/aluguel.csv', sep=';')
df.head(10)
# Vendo tipos das colunas e renomeando index
Tipo_dados = pd.DataFrame(df.dtypes, columns=['Tipo_Dados'])
Tipo_dados.columns.name = 'Colunas'
Tipo_dados
# Read Json
df_json = pd.read_json('arquivos_aula/dados/aluguel.json')
df_json
# Read txt (sep default tabulado)
df_txt = pd.read_table('arquivos_aula/dados/aluguel.txt')
df_txt
# Read excel xlsx
df_xlsx = pd.read_excel('arquivos_aula/dados/aluguel.xlsx')
df_xlsx