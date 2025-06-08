import matplotlib.pyplot as plt

# Classes et observations données
cl = [2, 3, 5, 7, 10]
Obs = [2, 10, 7, 5, 2, 7, 5, 7, 2, 2]

# Fonctions demandées
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

# Calcul des effectifs
effectifs = calcEffectif(cl, Obs)

# Affichage des résultats
print("Tableau des effectifs :", effectifs)

# Tracé du diagramme en bâtons
plt.bar(cl, effectifs, color='skyblue', edgecolor='black')
plt.xlabel("Valeurs de X")
plt.ylabel("Effectifs")
plt.title("Diagramme en bâtons des observations")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("../figures/diagramme_baton_exemple.png")
plt.show()
