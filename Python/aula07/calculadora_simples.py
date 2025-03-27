"""
Escreva um programa em Python que simule uma calculadora simples, contendo as quatro operações básicas (+, -, *, / - acrescente mais uma operação).

O programa deve ter:
- Menu de operações
- Realizar o cálculo escolhido (dois números)
- Apresentar o resultado
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /, **): ")

match operacao:
    case "+":
        print(f"Resultado: {num1 + num2}")
    case "-":
        print(f"Resultado: {num1 - num2}")
    case "*":
        print(f"Resultado: {num1 * num2}")
    case "/":
        if num2 == 0:
            print("Divisão por zero!")
        else:
            print(f"Resultado: {num1 / num2}")
    case "**":
        print(f"Resultado: {num1 ** num2}")
    case _:
        print("Operação inválida!")
