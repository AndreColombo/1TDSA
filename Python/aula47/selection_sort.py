"""
Algoritmos de Ordenação
- Selection Sort (ordenação por seleção)
    - Opera através de iterações - elemento por elemento
    - Realizando trocas, caso um elemento seja menor (ou maior) do que outro
    - A cada iteração, a parte ordenada é aumentada, enquanto não ordenada é diminuida

    - Complexidade O(n²)
"""

import time


def selection_sort(seq):
    """
    Ordena uma lista de números utilizando o algoritmo Selection Sort
    """
    n = len(seq)

    for i in range(n):
        indice_minimo = i

        for j in range(i + 1, n):
            if seq[j] < seq[indice_minimo]:
                indice_minimo = j

        # realiza a troca (atribuição paralela)
        seq[i], seq[indice_minimo] = seq[indice_minimo], seq[i]
    return seq


def tempo():
    print("Inicio...")
    inicio = time.time()
    for i in range(10):
        print(".")
        time.sleep(1)  # 1 seg
    fim = time.time()
    print("Fim...")
    print(f"Tempo: {fim-inicio}")


# Programa Principal
lista = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"Lista original: {lista}")
inicio = time.time()
selection_sort(lista)
fim = time.time()
print(f"Lista ordenada: {lista}")
print(f"Tempo: {fim-inicio}")
