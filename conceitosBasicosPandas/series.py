import pandas as pd
import numpy as np

# Criacao de dados
serie1 = pd.Series([1, 2, 3, 4], index=['EUA', 'Alemanha', 'Russia', 'Japao'])

# Plotagem dados
# print(serie1)

# Criacao de dados
serie2 = pd.Series([2, 3, 4, 5], index=['EUA', 'Alemanha', 'Russia', 'Japao'])

# Plotagem dados
# print(serie2)

# Acessando valores a partir do index
change_index = serie1['Japao']
# print(change_index)

# Acessando 2 valores a partir do index
change_index = serie1[['Japao', 'EUA']]
# print(change_index)


# Operacoes aritmeticas com series
soma = serie1 + serie2
# print(soma)

subtracao = serie2 - serie1
print(subtracao)
