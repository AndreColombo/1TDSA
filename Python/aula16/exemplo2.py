"""
Crie um programa em Python que leia 4 salários, calcue a média salarial e imprima os salários que estiverem abaixo da média
"""

salarios = [0, 0, 0, 0]
soma = 0
# Entadas de dados
salarios[0] = float(input("Salário R$: "))
soma += salarios[0]
salarios[1] = float(input("Salário R$: "))
soma += salarios[1]
salarios[2] = float(input("Salário R$: "))
soma += salarios[2]
salarios[3] = float(input("Salário R$: "))
soma += salarios[3]

# Cálculo da média salarial
media = soma / 4

print(f"Média salarial: {media:.2f}")

# Imprimir os salários que estão abaixo da média
if salarios[0] < media:
    print(f"Abaixo da média: {salarios[0]:.2f}")
if salarios[1] < media:
    print(f"Abaixo da média: {salarios[1]:.2f}")
if salarios[2] < media:
    print(f"Abaixo da média: {salarios[2]:.2f}")
if salarios[3] < media:
    print(f"Abaixo da média: {salarios[3]:.2f}")
