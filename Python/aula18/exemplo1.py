"""
Escreva um programa em Python que leia 5 nomes (armazene-os em uma lista) e exiba a quantidade de nomes que iniciam com VOGAL
"""

# criação da lista
nomes = []

# preenchendo (popular) a lista
for i in range(5):
    nome = input("Nome: ")
    nomes.append(nome)

# variável contadora
qtde = 0

# percorre a lista de nomes, verificando as iniciadas com VOGAL
for nome in nomes:
    if (
        nome[0] == "A"
        or nome[0] == "E"
        or nome[0] == "I"
        or nome[0] == "O"
        or nome[0] == "U"
    ):
        qtde += 1
print(f"Qtde: {qtde}")
