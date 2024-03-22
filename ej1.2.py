import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# coordenadas x e y
# 'ro' indica que los puntos se representarán como círculos rojos ('r' para el color rojo y 'o' para círculos)
plt.axis((0, 6, 0, 20))
# límites de los ejes del gráfico
plt.show()
# Muestra el gráfico