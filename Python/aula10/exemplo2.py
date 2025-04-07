total = 0
quero_comprar = True

while quero_comprar:
    item = float(input("Digite o valor do item comprado: "))
    total += item
    opcao = input("Continuar comprando? (s/n): ")
    if opcao != "s":
        quero_comprar = False

print(f"Total da compra: R${total:.2f}")
