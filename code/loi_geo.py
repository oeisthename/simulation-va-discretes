import random
import math
import matplotlib.pyplot as plt
import numpy as np

def Bernoulli(p):
    """Simule un essai de Bernoulli avec succès p."""
    return 1 if random.random() < p else 0

def geom(p):
    """Simule une variable aléatoire suivant la loi géométrique de paramètre p en utilisant Bernoulli."""
    count = 1
    while Bernoulli(p) == 0:
        count += 1
    return count

def geoinv(p):
    """Simule une variable aléatoire suivant la loi géométrique par méthode d'inversion."""
    U = random.random()
    return math.ceil(math.log(1 - U) / math.log(1 - p))

def loi_des_grands_nombres(p, N=10000):
    """Illustre la loi des grands nombres pour la loi géométrique."""
    samples = np.random.geometric(p, N)
    moyennes_cumulees = np.cumsum(samples) / np.arange(1, N+1)

    plt.plot(moyennes_cumulees, label='Moyenne empirique')
    plt.axhline(y=1/p, color='r', linestyle='--', label=f'Espérance théorique 1/p = {1/p}')
    plt.xlabel('Nombre de tirages')
    plt.ylabel('Moyenne cumulative')
    plt.title('Illustration de la loi des grands nombres (loi géométrique)')
    plt.legend()
    plt.grid(True)
    plt.show()

# --- Exemple d'utilisation ---

p = 0.3

# Simulation avec la fonction geom(p)
simulations_geom = [geom(p) for _ in range(1000)]

# Simulation avec la méthode d'inversion
simulations_geoinv = [geoinv(p) for _ in range(1000)]

# Histogramme des deux simulations
plt.hist(simulations_geom, bins=range(1, max(simulations_geom)+2), alpha=0.6, label='geom(p)')
plt.hist(simulations_geoinv, bins=range(1, max(simulations_geoinv)+2), alpha=0.6, label='geoinv(p)')
plt.xlabel('Valeurs simulées')
plt.ylabel('Effectifs')
plt.title(f'Simulation loi géométrique de paramètre p={p}')
plt.legend()
plt.show()

# Illustration de la loi des grands nombres
loi_des_grands_nombres(p)
