"""
Desenvolva o fluxograma e implemente um programa em Python que leia o nome
de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês
(em dinheiro). Sabendo que este vendedor recebe 20% de comissão sobre suas
vendas efetuadas entre segunda e quarta-feira, 15% para vendas efetuadas entre
quinta e sexta-feira e 10% para vendas realizadas aos sábados e domingos. Faça
um programa para calcular e imprimir o total a receber no final do mês.
"""

# Obter o nome do vendedor
# Obter o salário fixo
# Obter o total vendido nos períodos definindos
# Calcular 20% do total de vendas - seg_qua
# Calcular 15% do total de vendas - qui_sex
# Calcular 10% do total de vendas - sab-dom
# Apresentar o total a receber
print("*-- Exercício 1 - Calcular Comissão --*")

# entradas de dados
nome = input("Vendedor: ")
salario = float(input("Salário: "))
tv_seg_qua = float(input("Total vendas seg-qua: "))
tv_qui_sex = float(input("Total vendas quu-sex: "))
tv_sab_dom = float(input("Total vendas sab-dom: "))

# Processamento
comissao_seg_qua = tv_seg_qua * 0.2
comissao_qui_sex = tv_qui_sex * 0.15
comissao_sab_dom = tv_sab_dom * 0.1

total_comissao = comissao_seg_qua + comissao_qui_sex + comissao_sab_dom

total_receber = salario + total_comissao

# saída de dados
print(f"{nome}")
print(f"Salário fixo: {salario:.2f}")
print(f"Comissão: {total_comissao:.2f}")
print(f"Total a receber: {total_receber:.2f}")


"""
Desenvolva o fluxograma e implemente um programa em Python que leia o salário
de um funcionário e calcule o imposto de renda (IR) a ser pago a partir do salário
do funcionário, de acordo com a tabela abaixo:
• Para renda familiar até 1.903,98 - isento
• Para renda familiar entre 1.903,99 e 2.826,65 - alíquota de 7,5%
• Para renda familiar entre 2.826,66 e 3.751,05 - alíquota de 15%
• Para renda familiar entre 3.751,06 e 4.664,67 - alíquota de 22,5%
• Para renda familiar acima de 4.664,68 - alíquota de 27,5%
"""
print("*- Calculo do IR -*")

# entrada de dados
salario = float(input("Salário: "))
if salario < 0:
    print("Salário negativo")
elif salario <= 1903.98:
    print("Isento")
elif salario >= 1903.99 and salario <= 2826.65:
    ir = salario * 0.075
elif salario >= 2826.66 and salario <= 3751.05:
    ir = salario * 0.15
elif salario >= 3751.06 and salario <= 4664.67:
    ir = salario * 0.22
elif salario >= 4664.68:
    ir = salario * 0.275

# saída de dados
print(f"Salário: {salario:.2f} \nImposto: {ir} \nLíquido: {salario-ir}")
