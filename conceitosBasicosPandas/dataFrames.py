import pandas as pd
import numpy as np
from numpy.random import randn

# criacao da tabela (usando o metodo randn para criacao de dados aleatorios)
data_frame = pd.DataFrame(
    randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])

print(f'originalDataFrame:\n,{data_frame}')

# Selecao de uma coluna da tabela
# select_column = data_frame['W']
# print(select_column)

# Operacao aritimetica data frame
# data_frame['media'] = data_frame['W'] + data_frame['X']/2
# print(data_frame)

# deletando uma coluna
# data_frame2 = data_frame.drop('media', axis=1)
# print(data_frame)  # O original e sempre mantido
# print(data_frame2)  # Retorna com a coluna deletada
# data_frame2 = data_frame.drop('media', axis=1, inplace=True)
# print(data_frame)  # deleta a coluna na tabela original

# Acessando valores das linhas
linhas_AB = data_frame.loc[['A', 'B']]
print(f'selectedLines:\n{linhas_AB}')
