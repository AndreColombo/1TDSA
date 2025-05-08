print("FIAP")   # FIAP
x = 1
print(x)   # 1
nome = input("Nome: ")   # Nome: Fernando
nome   # 'Fernando'
pi   # Traceback (most recent call last):
     #   File "<pyshell#5>", line 1, in <module>
     #     pi
     # NameError: name 'pi' is not defined
math   # Traceback (most recent call last):
       #   File "<pyshell#6>", line 1, in <module>
       #     math
       # NameError: name 'math' is not defined. Did you forget to import 'math'?
import math

math   # <module 'math' (built-in)>
math.pi   # 3.141592653589793
math.pow(3, 3)   # 27.0
r = math.pow(2, 3)
print(r)   # 8.0
print(math.pow(2, 3))   # 8.0


def imprimir(var):
    print(f"Valor: {var}")


imprimir   # <function imprimir at 0x000001CD097F6D40>
imprimir("Gabriel")   # Valor: Gabriel
imprimir(10)   # Valor: 10
imprimir("Pedro")   # Valor: Pedro


def imprimir(var):
    for i in range(10):
        print(f"Valor: {var}")


imprimir("Pedro")
# Valor: Pedro
# Valor: Pedro
# Valor: Pedro
# Valor: Pedro
# Valor: Pedro
# Valor: Pedro
# Valor: Pedro
# Valor: Pedro
# Valor: Pedro
# Valor: Pedro
imprimir(3)
# Valor: 3
# Valor: 3
# Valor: 3
# Valor: 3
# Valor: 3
# Valor: 3
# Valor: 3
# Valor: 3
# Valor: 3
# Valor: 3


def imprimir(var, qtde):
    for i in range(qtde):
        print(f"Valor: {var}")


imprimir("Gabriel", 5)
# Valor: Gabriel
# Valor: Gabriel
# Valor: Gabriel
# Valor: Gabriel
# Valor: Gabriel

imprimir(10, 3)


# Valor: 10
# Valor: 10
# Valor: 10
def somar():
    n1 = int(input("Número: "))
    n2 = int(input("Número: "))
    soma = n1 + n2
    print(soma)


somar()   # Número: 1
          # Número: 2
          # 3
def somar(n1, n2):
    return n1 + n2


somar(2, 3)   # 5
r = somar(10, 20)
r   # 30


def somar(n1, n2):
    result = n1 + n2
    imprimir(result, 5)
    return result


n1 = int(input("Número: "))   # Número: 3
n2 = int(input("Número: "))   # Número: 5
somar(n1, n2)
# Valor: 8
# Valor: 8
# Valor: 8
# Valor: 8
# Valor: 8
# 8

r = somar(n1, n2)
# Valor: 8
# Valor: 8
# Valor: 8
# Valor: 8
# Valor: 8
print(r)   # 8
