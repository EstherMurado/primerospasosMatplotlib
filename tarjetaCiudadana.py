import pandas as pd
import io
import matplotlib.pyplot as plt

datos = pd.read_csv('./datos/tar_ciudadana.csv')
'''cantidad (y) de tarjetas por mes (x) y dos colores, para j y f'''

jota = datos.loc[datos['TIPO'] == 'J']
efe = datos.loc[datos['TIPO'] == 'F']

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
dato1 = efe['CUANTOS']
dato2 = jota['CUANTOS']
mesesJ = efe['MES'] # Usar unique() para obtener los meses únicos
mesesF = jota['MES']
#meses = datos['MES']

# x = range(len(meses))

# fig, ax = plt.subplots()
plt.figure(figsize=(10, 6))

'''
barras1 = ax.bar(x, dato1, width=0.4, color='purple', label='Tipo F')
# Dibujar las barras para Tipo J desplazadas
barras2 = ax.bar([i + 0.4 for i in x], dato2, width=0.4, color='orange', label='Tipo J')
'''

dato1.plot(kind='bar', width=0.2, color='purple', label='Tipo F')
dato2.plot(kind='bar', width=0.2, color='orange', label='Tipo J')

plt.title('Cantidad de Tarjetas por mes (2022)')
plt.xlabel('Mes')
plt.ylabel('Cantidad')

# Añadir etiquetas en el eje x
plt.xticks(meses)


plt.tight_layout()
print(mesesJ)
print(mesesF)

plt.show()
print(jota)
print(efe)
