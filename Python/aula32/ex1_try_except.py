"""
Tratamento de erros (try-except)
"""

while True:
    try:
        num = int(input("Número: "))
        if num < 0:
            break
    except ValueError:
        print("Entrada inválida! Por favor, digite um número")
