"""
Merge Sort - ordenação por intercalação ou fusão
- Algoritmo recursivo
- "dividir para conquistar"
- considerado um dos algoritmos mais eficientes de propósito geral

Complexidade: O(nlogn) - pior ou médio caso | O(n)
"""


def merge_sort(seq):
    """
    Merge Sort - Algoritmo de ordenação por intercalação
    """
    if len(seq) > 1:
        meio = len(seq) // 2  # divisão inteira

        # fatiamento
        L = seq[:meio]  # Left
        R = seq[meio:]  # Right

        # chamada recursiva
        merge_sort(L)
        merge_sort(R)

        # variáveis de controle
        # i - fará o controle da lista L (Left)
        # j - fará o controle da lista R (Right)
        # k - fará o controle da lista ANTERIOR à recursão (seq)
        i = j = k = 0

        # Lógica para fazer comparações e trocas
        while i < len((L)) and j < len(R):
            if L[i] < R[j]:
                seq[k] = L[i]
                i += 1
            else:
                seq[k] = R[j]
                j += 1
            k += 1

        # verificação dos elementos da lista L (Left)
        while i < len((L)):
            seq[k] = L[i]
            i += 1
            k += 1

        # verificação dos elementos da lista R (Right)
        while j < len((R)):
            seq[k] = R[j]
            j += 1
            k += 1
    return seq


# Programa Principal
lista = [38, 27, 43, 3, 9, 82, 10]
print(f"Lista original: {lista}")
merge_sort(lista)
print(f"Lista ordenada: {lista}")
