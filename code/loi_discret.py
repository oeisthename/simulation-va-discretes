import random
import matplotlib.pyplot as plt
import numpy as np

def sommeCumulee(P):
    """Calcule la somme cumulée des probabilités P."""
    r = []
    cumul = 0
    for p in P:
        cumul += p
        r.append(cumul)
    return r

def discreteQ(P, X):
    """Simule une variable aléatoire discrète selon la méthode d'inversion."""
    r = sommeCumulee(P)
    U = random.random()
    for k in range(len(r)):
        if U < r[k]:
            return X[k]
    return X[-1]

def trace_fonction_repartition(X, P):
    """Trace la fonction de répartition d'une variable discrète."""
    r = [0] + sommeCumulee(P)  # r0 = 0
    x_min = min(X) - 1
    x_max = max(X) + 1

    # Préparer les points pour la fonction en escalier
    xs = []
    ys = []

    xs.append(x_min)
    ys.append(0)

    for i in range(len(X)):
        xs.append(X[i])
        ys.append(r[i])
        xs.append(X[i])
        ys.append(r[i+1])

    xs.append(x_max)
    ys.append(1)

    plt.step(xs, ys, where='post')
    plt.xlabel('x')
    plt.ylabel('F_X(x)')
    plt.title('Fonction de répartition F_X pour une variable discrète')
    plt.grid(True)
    plt.show()

def simulation_et_tracé(P, X, N=1000):
    """Simule N tirages et trace le diagramme en bâtons des fréquences."""
    simulations = [discreteQ(P, X) for _ in range(N)]
    effectifs = [simulations.count(xi) for xi in X]
    frequences = np.array(effectifs) / N

    plt.bar(X, frequences, width=0.6, color='blue', alpha=0.7)
    plt.xlabel('Valeurs de X')
    plt.ylabel('Fréquence')
    plt.title(f'Simulation loi discrète avec {N} tirages')
    plt.show()

# --- Exemple pour loi uniforme discrète U{0,...,5} ---
X_uniforme = [0, 1, 2, 3, 4, 5]
P_uniforme = [1/6] * 6

# Tracé fonction de répartition
trace_fonction_repartition(X_uniforme, P_uniforme)

# --- Exemple pour loi discrète arbitraire ---
P_arbitraire = [0.3, 0.2, 0.4, 0.1]
X_arbitraire = [1, 2, 4, 5]

# Simulation + tracé diagramme en bâtons
simulation_et_tracé(P_arbitraire, X_arbitraire)
