import matplotlib.pyplot as plt

# Valeurs possibles (classes) et leurs effectifs
absc = [2, 3, 5, 7, 10]     # valeurs prises par la variable aléatoire
ord = [4, 0, 2, 3, 1]       # effectifs associés à ces valeurs

# Tracé du diagramme en bâtons
plt.bar(absc, ord, color='skyblue', edgecolor='black')

# Personnalisation du graphe
plt.xlabel("Valeurs de la variable X")
plt.ylabel("Effectifs")
plt.title("Diagramme en bâtons : v.a. discrète")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Enregistrement et affichage
plt.savefig("../figures/diagramme_bar_valeurs.png")
plt.show()
