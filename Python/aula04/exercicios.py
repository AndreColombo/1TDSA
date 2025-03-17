# ---------- Exercício 1 ----------
tempF = float(input("Digite a temperatura em Fahrenheit: "))
tepmC = print("Temperatura em Celsius: ", (tempF - 32)/1.8)

# ---------- Exercício 3 ----------
salario = float(input("Digite seu salário atual: "))
aumento = print("Seu salário com aumento é de: ", salario+(salario/10))

# ----------------------------------------

# ---------- Exercício 1 ----------
horas = float(input("Digite as horas de trabalho: "))
valorH = float(input("Digite o valor por hora: "))
salario = print("R$"+str(horas*valorH))

# ---------- Exercício 2 ----------
qntMin = float(input("Digite o mínimo do estoque: "))
qntMax = float(input("Digite o máximo do estoque: "))
media = print((qntMin+qntMax)/2)

# ---------- Exercício 3 ----------
num = float(input("Digite um número: "))
quadrado = print(num**2)

# ---------- Exercício 4 ----------
nA = float(input("Digite o 1° número: "))
nB = float(input("Digite o 2° número: "))
elevado = print(nA**nB)

# ---------- Exercício 5 ----------
cotDol = float(input("Digite a contação do Dólar: "))
qntDol = float(input("Digite quantos Dólares quer comprar: "))
valReal = print(cotDol*qntDol)

# ---------- Exercício 6 ----------
idVen = float(input("Digite a identificação do vendedor: "))
codPec = float(input("Digite o código da peça: "))
prcPec = float(input("Digite o preço da peça: "))
qntPec = float(input("Digite a quantidade de peças: "))
totalVen = prcPec*qntPec
comVen = totalVen/20
print("id: " + str(idVen) + ", Valor total da venda: " + str(totalVen) + ", Comissão da venda: " + str(comVen))