"""
Algoritmo Insrtion Sort (Ordenação por inserção)
- Complexidade: O(n²)
"""

import time


def insertion_sort(seq):
    """
    Função de ordenação Insertion Sort
    """
    n = len(seq)

    for i in range(1, n):
        ref = seq[i]
        j = i - 1
        while j >= 0 and ref < seq[j]:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = ref  # realiza a troca aqui


# Programa Princial
lista = [12, 11, 13, 5, 6]
print(f"Lista original: {lista}")
inicio = time.time()
insertion_sort(lista)
fim = time.time()
print(f"Lista ordenada: {lista}")
print(f"Tempo: {fim-inicio}")
