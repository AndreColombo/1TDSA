nome = input("Atleta: ")
saltos = []
resultados = []
media = 0

if nome != "":
    for salto in range(5):
        salto = float(input("Digite a distância do salto: "))
        resultados.append(salto)
        media += salto
    media = media / 5

    if (
        resultados[0] > resultados[1]
        and resultados[0] > resultados[2]
        and resultados[0] > resultados[3]
        and resultados[0] > resultados[4]
    ):
        maior = resultados[0]
    elif (
        resultados[1] > resultados[0]
        and resultados[1] > resultados[2]
        and resultados[1] > resultados[3]
        and resultados[1] > resultados[4]
    ):
        maior = resultados[1]
    elif (
        resultados[2] > resultados[0]
        and resultados[2] > resultados[1]
        and resultados[2] > resultados[3]
        and resultados[2] > resultados[4]
    ):
        maior = resultados[2]
    elif (
        resultados[3] > resultados[0]
        and resultados[3] > resultados[1]
        and resultados[3] > resultados[2]
        and resultados[3] > resultados[4]
    ):
        maior = resultados[3]
    else:
        maior = resultados[4]

    print(f"\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Saltos: {resultados}")
    print(f"Maior salto: {maior}")
    print(f"Média dos saltos: {media}")
else:
    print("Nome não informado")
