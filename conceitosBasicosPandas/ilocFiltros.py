import pandas as pd
import numpy as np
from numpy.random import randn

# criacao da tabela (usando o metodo randn para criacao de dados aleatorios)
data_frame = pd.DataFrame(
    randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])
print(data_frame)

# filtragem dos dados da tabela (filtros condicionais)
# selecionar na tabela valores maiores que 0
filtro = data_frame[data_frame > 0]
# print(filtro)

# filtrar na tabela valores menores que 0
filtro2 = data_frame[data_frame < 0]
# print(filtro2)
