import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Fonction de simulation
def uniforme(a, b):
    return a + math.floor(random.random() * ((b - a) + 1))

# Fonction utilitaire : calcEffectif
def position(L, elt):
    for i in range(len(L)):
        if L[i] == elt:
            return i
    return -1

def calcEffectif(cl, Obs):
    effectifs = [0] * len(cl)
    for val in Obs:
        i = position(cl, val)
        if i != -1:
            effectifs[i] += 1
    return effectifs

# Paramètres
N = 1000      # Nombre de simulations
a = 1
b = 4         # Uniforme sur {1, 2, 3, 4}
n = b - a + 1

#Ligne 9 équivalente avec une boucle for
Obs = []
for _ in range(N):
    Obs.append(uniforme(a, b))

# Classes
cl = list(range(a, b + 1))

#Calcul des effectifs
effectif = calcEffectif(cl, Obs)

#Distribution théorique
P = [1 / n] * n

#Tracé du diagramme comparatif
absc = np.array(cl)
plt.bar(absc, P, color='r', width=0.3, label="Théorique (U_d)")
plt.bar(absc + 0.3, [e / N for e in effectif], color='b', width=0.3, label="Expérimental")
plt.xlabel("Valeurs possibles")
plt.ylabel("Probabilités / Fréquences")
plt.title("Loi uniforme discrète sur {1, ..., 4}")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("../figures/hist_uniforme_discrete.png")
plt.show()
