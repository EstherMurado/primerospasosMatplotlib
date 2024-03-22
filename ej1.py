import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
# Si nos metemos en plot vemos que no está dentro de una clase, está haciendo cosas estáticas.
#Con ver que su primer parámetro no es un self
plt.ylabel('some numbers')
plt.show()
