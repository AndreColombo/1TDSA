salarios = []
soma = 0
i = 0  # var de controle

while i < 4:
    salario = float(input(f"Salário R$: "))
    soma += salario
    salarios.append(salario)
    i += 1

media = soma / 4
print(f"Média salarial: {media:.2f}")

i = 0
while i < 4:
    if salarios[i] < media:
        print(f"Abaixo da média: {salarios[i]:.2f}")
    i += 1
