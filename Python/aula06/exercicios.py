# ---------- Exercício 1 ----------
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
produto = print(num1 * num2)

# ---------- Exercício 2 ----------
base = float(input("Digite o primeiro número: "))
expoente = float(input("Digite o segundo número: "))
potencia = print(base**expoente)

# ---------- Exercício 3 ----------
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
quadrado1 = num1**2
quadrado2 = num2**2
soma = print(quadrado1 + quadrado2)

# ---------- Exercício 4 ----------
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
consecutivo1 = num1 + 1
consecutivo2 = num2 + 1
soma = print(f"Os consecutivos são: {consecutivo1} e {consecutivo2}")

# ---------- Exercício 5 ----------
ladoL = float(input("Digite o valor de L: "))
area = print(ladoL * ladoL)

# ---------- Exercício 6 ----------
numA = float(input("Digite o valor do lado A: "))
numB = float(input("Digite o valor do lado B: "))
numC = float(input("Digite o valor do lado C: "))
areaTriangulo = print("Área do triângulo retângulo: ", (numA * numC) / 2)
areaCirculo = print("Área do círculo: ", 3.14 * (numC**2))
areaTrapezio = print("Área do trapézio: ", ((numA + numB) * numC) / 2)
areaQuadrado = print("Área do quadrado: ", numB**2)
areaRetangulo = print("Área do retângulo: ", numA * numB)
perimetroRetangulo = print("Perímetro do retângulo: ", 2 * (numA + numB))

# ---------- Exercício 7 ----------
numA = int(input("Digite o valor do lado A: "))
numB = int(input("Digite o valor do lado B: "))
hipotenusa = print("O valor da hipotenusa é: ", (numA**2 + numB**2) ** (1 / 2))

# ---------- Exercício 8 ----------
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
mediaAritmetica = print("A média aritmética é: ", (num1 + num2 + num3 + num4) / 4)

# ---------- Exercício 9 ----------
numCadastro = int(input("Digite seu número de cadastros: "))
horas = float(input("Digite o número de horas trabalhadas: "))
valorHora = float(input("Digite o valor da hora trabalhada: "))
salario = horas * valorHora
print("Número de cadastros: ", numCadastro, "- Salário: ", salario)

# ---------- Exercício 10 ----------
nomeVendedor = input("Digite o nome do vendedor: ")
salarioFixo = float(input("Digite o salário fixo: "))
totalVendas = float(input("Digite o total de vendas: "))
comissão = totalVendas * 0.15
print(
    f"O vendedor {nomeVendedor} receberá um salário de R${salarioFixo + comissão:.2f}"
)

# ---------- Exercício 11 ----------
num = float(input("Digite um número: "))
if num < 0:
    print("Número negativo")

# ---------- Exercício 12 ----------
numL = float(input("Digite o valor de L: "))
numR = float(input("Digite o valor de R: "))
areaQuadrado = numL * numL
areaCirculo = 3.14 * (numR * numR)
if areaQuadrado > areaCirculo:
    print("Quadrado")
elif areaCirculo > areaQuadrado:
    print("Circulo")
else:
    print("Áreas iguais")

# ---------- Exercício 13 ----------
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

# ---------- Exercício 14 ----------
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    res = print(num1 / num2)
else:
    res = print(num2 / num1)

# ---------- Exercício 15 ----------
numA = float(input("Digite o primeiro número: "))
numB = float(input("Digite o segundo número: "))
numC = float(input("Digite o terceiro número: "))
delta = (numB**2) - (4 * numA * numC)
if numA == 0:
    print("Impossível calcular")
elif delta < 0:
    print("Impossível calcular")
else:
    bhaskara1 = (-numB + (delta**0.5)) / (2 * numA)
    bhaskara2 = (-numB - (delta**0.5)) / (2 * numA)
    print(f"As raízes da equação são {bhaskara1} e {bhaskara2}")

# ---------- Exercício 16 ----------
horaI = int(input("Digite a hora inicial: "))
horaF = int(input("Digite a hora final: "))
if horaI < horaF:
    duracao = horaF - horaI
else:
    duracao = (24 - horaI) + horaF

print(f"O jogo durou {duracao} horas(s)")

# ---------- Exercício 17 ----------
numA = int(input("Digite o primeiro número: "))
numB = int(input("Digite o segundo número: "))
numC = int(input("Digite o terceiro número: "))
numD = int(input("Digite o quarto número: "))
if (
    numB > numC
    and numD > numA
    and numC + numD > numA + numB
    and numC > 0
    and numD > 0
    and numA % 2 == 0
):
    print("Valores aceitos")
else:
    print("Valores não aceitos")

# ---------- Exercício 18 ----------
numA = float(input("Digite o primeiro número: "))
numB = float(input("Digite o segundo número: "))
numC = float(input("Digite o terceiro número: "))
decrescente = [numA, numB, numC]
decrescente.sort(reverse=True)
ladoA = decrescente[0]
ladoB = decrescente[1]
ladoC = decrescente[2]

if ladoA >= ladoB + ladoC:
    print("Não forma triângulo")
elif ladoA**2 == ladoB**2 + ladoC**2:
    print("Triângulo retângulo")
elif ladoA**2 > ladoB**2 + ladoC**2:
    print("Triângulo obtusângulo")
elif ladoA**2 < ladoB**2 + ladoC**2:
    print("Triângulo acutângulo")
elif ladoA == ladoB == ladoC:
    print("Triângulo equilátero")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print("Triângulo isósceles")
