continuar = True
while continuar:
    try:
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
        div = n1 / n2
        print(f"Resultado: {div:.2f}")
    except ZeroDivisionError:
        print("Erro - Divisão por ZERO!")
    except ValueError:
        print("Entrada inválida!")
    finally:  # opcional
        teste = int(input("1 - continuar? "))
        if teste != 1:
            continuar = False
