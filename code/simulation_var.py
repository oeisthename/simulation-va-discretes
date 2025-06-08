import random
import matplotlib.pyplot as plt

# Simulation de 10000 réalisations d'une variable aléatoire uniforme sur [0, 1[
n = 10000
echantillons = [random.random() for _ in range(n)]

# Affichage de quelques réalisations
print("Quelques réalisations de X ~ U[0,1[ :")
print(echantillons[:10])

# Visualisation : histogramme de fréquence
plt.hist(echantillons, bins=50, color='skyblue', edgecolor='black', density=True)
plt.axhline(y=1, color='red', linestyle='--', label='Densité théorique de U[0,1[')
plt.title("Histogramme des réalisations de X ~ U[0,1[")
plt.xlabel("Valeur")
plt.ylabel("Fréquence")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../figures/hist_uniforme_observations.png")
plt.show()
