salario_funcionario = float(input("Digite o salário do funcionário: "))

if salario_funcionario <= 1903.98:
    print(f"Isento do Imposto de Renda!\nSalário Líquido: {salario_funcionario}")
elif salario_funcionario >= 1903.99 and salario_funcionario <= 2826.65:
    imposto = salario_funcionario * 0.075
    salario_liquido = salario_funcionario - imposto
    print(
        f"Salário Bruto: {salario_funcionario}\nSalário Líquido: {salario_liquido}\nImposto: {imposto}"
    )
elif salario_funcionario >= 2826.66 and salario_funcionario <= 3751.05:
    imposto = salario_funcionario * 0.15
    salario_liquido = salario_funcionario - imposto
    print(
        f"Salário Bruto: {salario_funcionario}\nSalário Líquido: {salario_liquido}\nImposto: {imposto}"
    )
elif salario_funcionario >= 3751.06 and salario_funcionario <= 4664.68:
    imposto = salario_funcionario * 0.225
    salario_liquido = salario_funcionario - imposto
    print(
        f"Salário Bruto: {salario_funcionario}\nSalário Líquido: {salario_liquido}\nImposto: {imposto}"
    )
else:
    imposto = salario_funcionario * 0.275
    salario_liquido = salario_funcionario - imposto
    print(
        f"Salário Bruto: {salario_funcionario}\nSalário Líquido: {salario_liquido}\nImposto: {imposto}"
    )
