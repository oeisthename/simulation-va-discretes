import random
import math
import matplotlib.pyplot as plt
from collections import Counter

def Bernoulli(p):
    """Simule un essai Bernoulli avec succès p."""
    return 1 if random.random() < p else 0

def poissonRare(lmbda, n=1000):
    """
    Simule une variable aléatoire approchant la loi de Poisson P(lambda)
    par la loi binomiale B(n, p) avec p = lambda/n.
    """
    p = lmbda / n
    # Somme de n essais Bernoulli indépendants de paramètre p
    somme = 0
    for _ in range(n):
        somme += Bernoulli(p)
    return somme

# --- Exemple d'utilisation ---

lmbda = 4  # paramètre lambda de la loi de Poisson
n = 1000   # grand n pour approximation

# Simulation de 10000 variables suivant la loi approchée
simulations = [poissonRare(lmbda, n) for _ in range(10000)]

# Comptage des occurrences
freq = Counter(simulations)

# Préparation des données pour affichage
x_vals = sorted(freq.keys())
y_vals = [freq[k]/10000 for k in x_vals]

# Affichage du diagramme en bâtons de la distribution simulée
plt.bar(x_vals, y_vals, alpha=0.7, label='Simulation binomiale approchée')

# Affichage de la vraie loi de Poisson (formule)
poisson_pmf = [math.exp(-lmbda) * (lmbda**k) / math.factorial(k) for k in x_vals]
plt.plot(x_vals, poisson_pmf, 'ro-', label='Loi de Poisson théorique')

plt.xlabel('k')
plt.ylabel('P(X=k)')
plt.title(f'Approximation loi de Poisson P({lmbda}) via loi binomiale B(n={n}, p={lmbda/n:.4f})')
plt.legend()
plt.grid(True)
plt.show()
