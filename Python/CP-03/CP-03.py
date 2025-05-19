# André - 563112, José Diogo - 562341

"""
    Um sistema de monitoramento de temperaturas está em operação em uma cidade no
sudeste brasileiro, porém, é preciso melhorá-lo e expandir o seu uso para outras cidades.
Para isto, você foi contratado para desenvolver um novo sistema em Python que faça o
mapeamento das temperaturas médias em um determinado período e que seja capaz de
dar algumas informações sobre esses dados.
    Como parte dos requisitos, o programa deve coletar algumas temperaturas médias
(diárias), durante um período determinado pelo usuário (mapeados em dias), permita a
impressão de todas as temperaturas mapeadas, a maior e a menor temperatura lida, a
média das temperaturas mapeadas, e uma lista com as temperaturas negativas. Para isso,
escreva um programa que tenha:

• 1) Uma função que solicite ao usuário qual o período será mapeado (em dias)
• 2) Uma função para mapear/coletar as temperaturas em uma matriz (em dias)
• 3) Uma função para obter a maior e a menor temperatura mapeada no período
• 4) Uma função para ‘separar’ (em uma lista) as temperaturas negativas no período
mapeado
• 5) Uma função para obter a temperatura média no período
• 6) Função principal para testar o programa
"""


# 1) Uma função que solicite ao usuário qual o período será mapeado (em dias)
def periodoMapeamento():
    periodo = int(
        input("Insira qual periodo em dias que deseja que faça o mapeamento: ")
    )
    return periodo


# 2) Uma função para mapear/coletar as temperaturas em uma matriz (em dias)
def mapearTemperaturas(periodo):
    temperaturas = []
    i = 0
    while i < periodo:
        temperatura = float(input("Temperatura: "))
        temperaturas.append(temperatura)
        i += 1
    return temperaturas


# 3) Uma função para obter a maior e a menor temperatura mapeada no período
def maiorMenorTemperatura(temperaturas, periodo):
    maior = 0
    menor = 0
    i = 0
    while i < periodo:
        if maior < temperaturas[i]:
            maior = temperaturas[i]
        i += 1
    i = 0
    while i < periodo:
        if menor > temperaturas[i]:
            menor = temperaturas[i]
        i += 1
    return maior, menor


# 4) Uma função para ‘separar’ (em uma lista) as temperaturas negativas no período
def listaTemperaturaNegativa(temperaturas):
    listaTemperaturaNegativa = []
    for itemTemperatura in temperaturas:
        if itemTemperatura < 0:
            listaTemperaturaNegativa.append(itemTemperatura)
            print(
                f"Temperatura {itemTemperatura} adicionada a lista de temperaturas negativas."
            )
    return listaTemperaturaNegativa


# 5) Uma função para obter a temperatura média no período
def temperaturaMedia(temperaturas, periodo):
    soma = 0
    for item in temperaturas:
        soma += item
    media = soma / periodo
    return media


# 6) Função principal para testar o programa
def main():
    print("\n+-------- Progama monitoramento de temperaturas --------+\n")
    periodo = periodoMapeamento()  # parte 1
    temperaturas = mapearTemperaturas(periodo)  # parte 2
    print(temperaturas)
    print(maiorMenorTemperatura(temperaturas, periodo))  # parte 3
    print(listaTemperaturaNegativa(temperaturas))  # parte 4
    print(temperaturaMedia(temperaturas, periodo))  # parte 5


# Principal
main()
