import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos del archivo CSV
datos = pd.read_csv('datos/eventos_deportivos.csv', delimiter=';')

# Contar la cantidad de actividades deportivas para cada fecha
actividades_por_fecha = datos['FECHA'].value_counts().sort_index()

# Crear el gráfico de barras
# Tamaño ventana:
plt.figure(figsize=(10, 6))

actividades_por_fecha.plot(kind='bar', color='skyblue')
plt.title('Cantidad de Eventos por Fecha')
plt.xlabel('Fecha')
plt.ylabel('Cantidad Eventos')

plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x 45º pa leerlo mejor
plt.tight_layout() # Mejora la disposición y la estética de los subplots en una figura
plt.show()
