def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


# Main
lista = [12, 11, 13, 5, 6]
print(f"Soma: {soma(lista)}")
