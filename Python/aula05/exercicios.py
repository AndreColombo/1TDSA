# ---------- Exercício 1 ----------
numero = float(input("Digite um número: "))

if numero > 100:
    resultado = numero + 150
    print("Resultado: ", resultado)
else:
    print("Resultado: ", numero)

# ---------- Exercício 2 ----------
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 % num2 == 0:
    print("A divisão de", num1, "por", num2, " é exata")
else:
    print("A divisão de", num1, "por", num2, " não é exata")

# ---------- Exercício 3 ----------
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
massa = peso / (altura**2)

if massa < 26:
    print("Normal com massa: ", massa)
elif massa >= 26 and massa < 30:
    print("Obeso com massa: ", massa)
else:
    print("Obeso Mórbido com massa: ", massa)

# ---------- Exercício 4 ----------
kWh = float(input("Digite quantos KWk você consumiu: "))
if kWh < 150:
    valor = kWh * 0.20
    print("O valor da conta de energia será: ", valor)
elif kWh >= 150 and kWh < 500:
    valor = kWh * 0.25
    print("O valor da conta de energia será: ", valor)
else:
    valor = kWh * 0.30
    print("O valor da conta de energia será: ", valor)
