import matplotlib.pyplot as plt

# Datos para las barras
datos1 = [10, 15, 20, 25, 30]
datos2 = [15, 20, 25, 30, 35]
etiquetas = ['A', 'B', 'C', 'D', 'E']

# Ancho de las barras
ancho_barra = 0.35

# Coordenadas x para las barras
x = range(len(etiquetas))

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Dibujar las barras con dos colores
barras1 = ax.bar(x, datos1, width=ancho_barra, color='blue', label='Dato 1')
barras2 = ax.bar(x, datos2, width=ancho_barra, color='orange', label='Dato 2', bottom=datos1)

# Añadir etiquetas en el eje x
ax.set_xticks(x)
ax.set_xticklabels(etiquetas)

# Añadir leyenda
ax.legend()

# Mostrar el gráfico
plt.show()