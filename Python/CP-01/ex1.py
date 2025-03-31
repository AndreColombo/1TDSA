nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o valor do salário fixo: "))
total_vendasSQ = float(input("Digite o valor das vendas entre Segunda e Quarta: "))
total_vendasQS = float(input("Digite o valor das vendas entre Quinta e Sexta: "))
total_vendasSD = float(input("Digite o valor das vendas entre Sábado e Domingo: "))

comissao_SQ = total_vendasSQ * 0.20
comissao_QS = total_vendasSQ * 0.15
comissao_SD = total_vendasSQ * 0.10
comissao_Total = comissao_SQ + comissao_QS + comissao_SD

salario_final = salario_fixo + comissao_Total

print(f"O vendedor {nome_vendedor} tem um total de {salario_final} a receber.")
