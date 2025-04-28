salarios = []
soma = 0

for i in range(4):
    salario = float(input(f"Salário R$: "))
    soma += salario
    salarios.append(salario)

media = soma / 4
print(f"Média salarial: {media:.2f}")

for salario in salarios:
    if salario < media:
        print(f"Abaixo da média: {salario:.2f}")
