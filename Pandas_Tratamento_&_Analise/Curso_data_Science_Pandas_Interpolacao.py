import pandas as pd
data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
s
# Os comandos abaixo podem necessitar no inplace = True para salvar as modificacoes na variavel, 
# neste caso nao vamos utilizar para ficar mais didatico
# Atribuir valores em campos nulos
s.fillna(0)
# Utilizar ultimo nao nulo - asc 
# OBs: s.fillna(method = 'ffill', limit = 1) --- posso limitar a quantidade maxima de vezes que posso substituir
s.fillna(method = 'ffill') 
# Utilizar ultimo nao nulo - desc
s.fillna(method = 'bfill')
# Preencher vazios com a media da serie
s.fillna(s.mean())