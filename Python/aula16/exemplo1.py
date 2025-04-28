"""
Crie um programa em Python que leia 4 salários, calcue a média salarial e imprima os salários que estiverem abaixo da média
"""

soma = 0
# Entadas de dados
salario_1 = float(input("Salário R$: "))
soma += salario_1
salario_2 = float(input("Salário R$: "))
soma += salario_2
salario_3 = float(input("Salário R$: "))
soma += salario_3
salario_4 = float(input("Salário R$: "))
soma += salario_4

# Cálculo da média salarial
media = soma / 4

print(f"Média salarial: {media:.2f}")

# Imprimir os salários que estão abaixo da média
if salario_1 < media:
    print(f"Abaixo da média: {salario_1:.2f}")
if salario_2 < media:
    print(f"Abaixo da média: {salario_2:.2f}")
if salario_3 < media:
    print(f"Abaixo da média: {salario_3:.2f}")
if salario_4 < media:
    print(f"Abaixo da média: {salario_4:.2f}")
