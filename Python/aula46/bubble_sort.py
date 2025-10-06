# Algoritmo Bubble Sort
# Complexidade: O(n²)


def bubble_sort(seq):
    tam = len(seq)
    for i in range(tam - 1):
        troca = False  # flag de controle
        for j in range(0, tam - i - 1):
            if seq[j] > seq[j + 1]:
                troca = True
                seq[j], seq[j + 1] = seq[j + 1], seq[j]  # atribuição paralale
        # se não for necessário realizar a troca, o programa irá sair do loop
        if troca == False:  # if not troca:
            return


# Programa Principal
lista = [39, 12, 18, 85, 72, 10, 2, 18]
print(f"Lista original: {lista}")
bubble_sort(lista)  # função com efeito colateral
print(f"Lista ordenada: {lista}")
