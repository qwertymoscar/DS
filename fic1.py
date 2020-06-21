import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

fig = plt.figure()
ax = plt.axes()
x = np.linspace(0,10,1000)

ax.plot(x, np.sin(x))




# Chanegr la taille de police par défaut
plt.rcParams.update({'font.size': 15})

fig = plt.figure()
ax = plt.axes()
# Couleur spécifiée par son nom, ligne solide
plt.plot(x, np.sin(x - 0), color='blue', linestyle='solid', label='bleu')
# Nom court pour la couleur, ligne avec des traits
plt.plot(x, np.sin(x - 1), color='g', linestyle='dashed', label='vert')
# Valeur de gris entre 0 et 1, des traits et des points
plt.plot(x, np.sin(x - 2), color='0.75', linestyle='dashdot', label='gris')
# Couleur spécifié en RGB, avec des points
plt.plot(x, np.sin(x - 3), color='#FF0000', linestyle='dotted', label='rouge')

# Les limites des axes, essayez aussi les arguments 'tight' et 'equal' 
# pour voir leur effet
plt.axis([-1, 11, -1.5, 1.5])

# Les labels
plt.title("Un exemple de graphe")

# La légende est générée à partir de l'argument label de la fonctio
# plot. L'argument loc spécifie le placement de la légende
plt.legend(loc='lower left')

# Titres des axes
ax = ax.set(xlabel='x', ylabel='sin(x)')





# Numpy
"""
#entier = np.zeros(3, 'int')
#entier = np.array([range(i, i + 3) for i in [2, 4, 6]])
#x1 = np.random.randint(10, size=3)  # Tableau de dimension 1
#print(x1)
 rint(x1[-1])

x2 = np.random.randint(10, size=(2,3))
print(x2)
a = np.vstack([x1, x2])
print(a)

x = np.arange(3)
print(np.where(x>5))

M = np.random.random((3, 4))
print(M)
print("La somme de tous les éléments de M: ", M.sum())
print("Les sommes des colonnes de M: ", M.sum(axis=0))


b = np.arange(3)[:, np.newaxis]
print(x)
print(a)
print(b)
print(x+b) """