import pandas as pd
df = pd.read_csv("arquivos_aula/aluguel_residencial.csv", sep = ";")
df['Valor m2'] = (df['Valor']/df['Area']).round(2)
casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
df['Tipo Agregado'] = df['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')
df.to_csv("arquivos_aula/agrupar_residencial.csv", sep = ";", index = False)