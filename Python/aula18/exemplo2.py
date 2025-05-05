"""
Escreva um programa em Python que leia 5 nomes (armazene-os em uma lista) e exiba a quantidade de nomes que iniciam com VOGAL
"""

# criação da lista
nomes = []
nomes_vogal = []

# preenchendo (popular) a lista
for i in range(5):
    nome = input("Nome: ")
    nomes.append(nome)

# variável contadora
qtde = 0

# percorre a lista de nomes, verificando as iniciadas com VOGAL
for nome in nomes:
    if nome[0] in "AEIOU" or nome[0] in "aeiou":
        qtde += 1
        nomes_vogal.append(nome)
print(f"Qtde: {qtde}")
print(nomes_vogal)

print("\n--------------------------------\n")

for nome in nomes_vogal:
    print(f"Nome: {nome}")
