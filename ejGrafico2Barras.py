import pandas as pd
import matplotlib.pyplot as plt

# Ejemplo de datos
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
datos_tipo1 = [100, 120, 90, 110, 95]
datos_tipo2 = [90, 110, 100, 105, 115]

# Coordenadas x para las barras
x = range(len(meses))

# Ancho de las barras
ancho_barra = 0.4

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Dibujar las barras para Tipo 1
barras1 = ax.bar(x, datos_tipo1, width=ancho_barra, color='purple', label='Tipo 1')

# Dibujar las barras para Tipo 2 desplazadas
barras2 = ax.bar([i + ancho_barra for i in x], datos_tipo2, width=ancho_barra, color='orange', label='Tipo 2')

# Añadir etiquetas en el eje x
ax.set_xticks([i + ancho_barra / 2 for i in x])
ax.set_xticklabels(meses)

# Añadir leyenda
ax.legend()

# Mostrar el gráfico
plt.show()