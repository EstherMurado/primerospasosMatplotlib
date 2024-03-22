import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('./datos/tar_ciudadana.csv')

# Convertir el mes de formato numérico a formato de nombre de mes
datos['MES'] = pd.to_datetime(datos['MES'], format='%m').dt.strftime('%B')

# Agrupar los datos por mes y tipo, y sumar las cantidades de tarjetas
datos_agrupados = datos.groupby(['MES', 'TIPO'])['CUANTOS'].sum().unstack(fill_value=0)

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficar las barras para Tipo F y Tipo J
datos_agrupados.plot(kind='bar', stacked=True, color=['purple', 'orange'])

# Configurar título y etiquetas de ejes
plt.title('Cantidad de Tarjetas por mes (2022)')
plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)  # Rotar los nombres de los meses para mejor visualización

# Mostrar leyenda
plt.legend(title='Tipo')

# Ajustar diseño y mostrar la gráfica
plt.tight_layout()
plt.show()
