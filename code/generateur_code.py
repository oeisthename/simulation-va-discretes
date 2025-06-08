# Implémentation d'un générateur pseudo-aléatoire simple basé sur le modèle (S, f, s)

# Définir les paramètres du générateur
M = 2**31 - 1      # Grand entier (taille de S)
a = 16807          # Coefficient multiplicatif (f)
c = 0              # Incrément (si ≠ 0 : congruentiel linéaire complet)
s = 42             # Graine initiale

# Fonction f : f(x) = (a * x + c) % M
def f(x):
    return (a * x + c) % M

# Fonction g : normalisation dans [0, 1[
def g(x):
    return x / M

# Génération de la suite (xn), puis (g(xn))
def generate_sequence(seed, n):
    sequence_raw = []
    sequence_uniform = []
    x = seed
    for _ in range(n):
        x = f(x)
        sequence_raw.append(x)
        sequence_uniform.append(g(x))
    return sequence_raw, sequence_uniform

# Point d'entrée
if __name__ == "__main__":
    n = 10
    raw, uniform = generate_sequence(seed=s, n=n)

    print("Suite (xₙ) brute :")
    print(raw)

    print("\nSuite (g(xₙ)) normalisée ∈ [0, 1[ :")
    print(uniform)
