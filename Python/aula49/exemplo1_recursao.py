"""
Recursão - conceito de programação no qual uma função
chama a si mesma, para resolver um problema específico.

Componentes essenciais da recursão:
- case base: condição de parada
- passo recursão (step)

menu() >>> add() >> menu() >>> sub() >>> menu() >>> mult()
"""


# Exemplo 1: Somatório de todos os elementos de uma lista (recursivo)
def somatorio(lista):
    if len(lista) == 1:  # caso base (condição de parada)
        return lista[0]
    else:
        return lista[0] + somatorio(lista[1:])


# Exemplo 2: Cálculo do fatorial de um número (recursivo)
# 5! -> 5*4*3*2*1 = 120
# 0! = 1
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


# Programa Principal
lista = [1, 3, 5, 7, 9]
print(f"Soma: {somatorio(lista)}")
print(f"Fatorial: {fatorial(5)}")
