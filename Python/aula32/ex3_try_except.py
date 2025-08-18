lista = [1, 2, 3]

for i in lista:
    print(f"i: {i}")

try:
    print(lista[a])
except IndexError:
    print("Erro: o índice da lista está fora da faixa!")
except Exception as e:
    print(f"Erro genérico: {e}")
