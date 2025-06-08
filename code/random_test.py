import random

# Q1 : Génération d'un nombre aléatoire sans seed
print("random.random() sans seed :")
print(random.random())

# Q2 : Fixer une graine (seed) et observer la suite
random.seed(0)
print("\nSuite aléatoire après random.seed(0) :")
for _ in range(5):
    print(random.random())

# Q3 : Refaire la même chose avec la même graine (seed)
random.seed(0)
print("\nReproduction de la suite avec seed(0) à nouveau :")
for _ in range(5):
    print(random.random())
