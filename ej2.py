import matplotlib.pyplot as plt
import numpy as np

# Creamos diccionario llamado 'data'
data = {'a': np.arange(50),
        # Array de NumPy que va desde 0 hasta 49.
        'c': np.random.randint(0, 50, 50),
        # Array de NumPy de 50 números enteros aleatorios en el rango de 0 a 49 (exclusivo).
        'd': np.random.randn(50)}
        # Array de NumPy de 50 números aleatorios distribuidos normalmente (distribución gaussiana estándar).

data['b'] = data['a'] + 10 * np.random.randn(50)
# Los valores de 'b' se generan agregando un ruido aleatorio al arreglo 'a'.
data['d'] = np.abs(data['d']) * 100
# Los valores en la entrada 'd' del diccionario data se convierten en valores absolutos y luego se multiplican por 100.
# Esto asegura que todos los valores en 'd' sean positivos y los escala por un factor de 100.

plt.scatter('a', 'b', c='c', s='d', data=data)
# Crea un gráfico de dispersión usando los datos del dict 'data':
# indicando que los valores en 'a' serán mapeados en el
# eje x y los valores en 'b' serán mapeados en el eje y.

# c='c': Indica que los colores de los puntos serán determinados por los valores en 'c'
# s='d': Indica que el tamaño de los puntos será determinado por los valores en 'd'
# data=data: Especifica que los datos utilizados para el gráfico se encuentran en el diccionario data.

plt.xlabel('entry a')
# Establece la etiqueta del eje x como "entry a".
plt.ylabel('entry b')
# Establece la etiqueta del eje y como "entry b".
plt.show()