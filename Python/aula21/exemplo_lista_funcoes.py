"""
- Manipulação de listas com funções
- Documentação docstrings

1) Função para definir tamanho da lista
2) Função para criar e preencher a lista
3) Função para percorrer e imprimir os elementos da lista
4) Função para somar todos os elementos da lista
5) Função para imprimir os elementos pares da lista
6) Função para imprimir os elementos ímpares da lista
7) Função para retornar os elementos pares
8) Função principal para testar o programa

"""


def tamanho_lista():
    """ "
    Obter e retornar o tamanho da lista

    Parametros:
    - não tem parâmetros

    Retorno:
    - retorna um número inteiro - representando o tamanho da lista
    """
    print("*-- TAMANHO DA LISTA --*")
    print("-----------------------")
    n = int(input("Tamanho: "))
    return n


def criar_lista(t):
    """
    Criar e preencher a lista com números inteiros

    Parametros:
    - t: inteiro - representa o tamanho da lista

    Retorno:
    - retorna uma lista preenchida com números inteiros
    """
    print(f"*-- CRIAR LISTA com {t} elementos --*")
    print("--------------------------------------")
    lista = []  # criando uma lista vazia
    i = 0  # variável de controle

    # preenchendo a lista
    while i < t:
        n = int(input(f"Número: "))
        lista.append(n)
        i += 1
    return lista


def imprimir(lista):
    """
    Imprimir os elementos da lista

    Parametros:
    - lista: lista - lista a ser impressa

    Retorno:
    - não tem retorno
    """
    print("*-- IMPRIMINDO os ELEMENTOS da LISTA --*")
    print("----------------------------------------")
    for n in lista:
        print(f"Número: {n}")


def somar_elementos(lista):
    """
    Somar todos os elementos da lista

    Parametros:
    - lista: lista - lista a ser somada

    Retorno:
    - retorna a soma dos elementos da lista
    """
    print("*-- SOMANDO os ELEMENTOS da LISTA --*")
    print("-------------------------------------")
    soma = 0
    for n in lista:
        soma += n
    return soma


def imprimir_pares(lista):
    """
    Imprimir os elementos pares da lista

    Parametros:
    - lista: lista - lista a ser impressa

    Retorno:
    - não tem retorno
    """
    print("*-- IMPRIMINDO os PARES --*")
    print("---------------------------")
    for n in lista:
        if n % 2 == 0:
            print(f"{n} é PAR!")


def imprimir_impares(lista):
    """
    Imprimir os elementos ímpares da lista

    Parametros:
    - lista: lista - lista a ser impressa

    Retorno:
    - não tem retorno
    """
    print("*-- IMPRIMINDO os ÍMPARES --*")
    print("-----------------------------")
    for n in lista:
        if n % 2 != 0:
            print(f"{n} é ÍMPAR!")


def separar_pares(lista):
    """
    Retornar os elementos pares da lista

    Parametros:
    - lista: lista - lista a ser separada

    Retorno:
    - retorna uma lista com os elementos pares
    """
    print("*-- SEPARANDO os PARES --*")
    print("--------------------------")
    lista_pares = []
    for n in lista:
        if n % 2 == 0:
            lista_pares.append(n)
    return lista_pares


def princial():
    print("-----------------")
    print("*** PRINCIPAL ***")
    print("-----------------")
    t = tamanho_lista()
    lista = criar_lista(t)
    imprimir(lista)
    print(f"SOMA: {somar_elementos(lista)}")
    imprimir_pares(lista)
    imprimir_impares(lista)
    print(f"Lista PARES: {separar_pares(lista)}")


# Principal
princial()
