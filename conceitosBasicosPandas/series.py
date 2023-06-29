import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']

minha_lista = [10, 20, 30]

arr = np.array([10, 20, 30])

d = {'a': 10, 'b': 20, 'c': 30}


result = pd.Series(labels)

print(result)

function = pd.Series(data=labels, index=minha_lista)
print(function)
