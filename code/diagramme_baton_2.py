import random
import numpy as np
import matplotlib.pyplot as plt
from math import comb

# 1. Fonctions de simulation

def Bernoulli(p):
    """Simule une variable aléatoire Bernoulli B(p)"""
    return 1 if random.random() < p else 0

def binomiale(n, p):
    """Simule une variable aléatoire binomiale B(n, p)"""
    return sum(Bernoulli(p) for _ in range(n))


# 2. Paramètres

N = 1000   # nombre de simulations
n = 40     # nombre d'essais
p = 0.3    # probabilité de succès

# 3. Simulation des variables binomiales

Obs = []
for _ in range(N):
    Obs.append(binomiale(n, p))

# 4. Calcul des effectifs observés

effectif = np.array([Obs.count(k) for k in range(n+1)])

# 5. Calcul de la distribution théorique

P = np.zeros(n+1)
for k in range(n+1):
    comb_val = comb(n, k)          # ligne 18 complétée ici
    P[k] = comb_val * (p**k) * ((1-p)**(n-k))

# 6. Tracé des diagrammes en bâtons

absc = np.arange(n+1)  # abscisses : valeurs 0,1,...,n

plt.bar(absc, P, color='r', width=0.4, label='Théorique')
plt.bar(absc + 0.4, effectif / N, color='b', width=0.4, label='Simulé')

plt.xlabel('Nombre de succès k')
plt.ylabel('Probabilité / Fréquence')
plt.title('Loi Binomiale B({}, {}) : Théorique vs Simulation'.format(n, p))
plt.legend()
plt.show()
