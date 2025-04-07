"""
Escreva um programa que receba um crédito e depois, o preço de itens comprados por um cliente. O prgrama deverá parar de solicitar novos preços quando o crédito disponível for insuficiente para pagar por um item.

Ao final, o programa deve exibir o total da compra e o crédito restante.
"""

credito = float(input("Informe o crédito disponível: "))
total = 0  # variável acumuladora
item = float(input("Digite o valor do item comprado: "))

while credito >= item:
    total += item
    credito -= item
    print(f"Crédito restante: R${credito:.2f} \n")
    item = float(input("Digite o valor do item comprado: "))

print(f"Total da compra: R${total:.2f}")
print(f"Crédito restante: R${credito:.2f}")
