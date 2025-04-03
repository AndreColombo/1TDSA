# ---------- Exercício 1 ----------
i = 0
while i < 50:
    i = i + 1
    print(i)

# ---------- Exercício 2 ----------
n = int(input("Digite um valor para N: "))
i = 1
soma = 0

while i <= n:
    soma += i
    i += 1
print(soma)

# ---------- Exercício 3 ----------
# loop 'for' não ensinado

# ---------- Exercício 4 ----------
# loop 'for' não ensinado

# ---------- Exercício 5 ----------
# loop 'for' não ensinado

# ---------- Exercício 6 ----------
# loop 'do-while' não ensinado

# ---------- Exercício 7 ----------
i = 0
while i < 200:
    print(i)
    i = i + 7

# ---------- Exercício 8 ----------
i = 14
soma = 0
quantidade = 0

while i < 73:
    if i % 2 == 0:
        soma += i
        quantidade += 1
    i += 1

media = soma / quantidade
print(f"Média dos pares entre 13 e 73: {media}")

# ---------- Exercício 9 ----------
quantidade = int(input("Digite a quantidade de alunos: "))
contador = 0
soma = 0

while contador < quantidade:
    nota = float(input("Digite a nota do aluno: "))
    soma += nota
    contador += 1

media = soma / quantidade
print(f"Média da turma: {media}")

# ---------- Exercício 10 ----------
i = 1
soma = 0.0

while i <= 20:
    soma += 1 / i
    i += 1

print(f"Resultado da soma: {soma}")

# ---------- Exercício 11 ----------
n = int(input("Digite o valor de N: "))
i = 1
soma = 0.0

while i <= n:
    if i % 2 == 0:
        soma -= 1 / i
    else:
        soma += 1 / i
    i += 1

print(f"Resultado da soma: {soma}")

# ---------- Exercício 12 ----------
n = int(input("Digite o valor de N: "))
i = 1
soma = 0.0

while i <= n:
    numerador = i
    denominador = n - i + 1
    soma += numerador / denominador
    i += 1

print(f"Resultado da soma: {soma}")

# ---------- Exercício 13 ----------
n = int(input("Digite o valor de N: "))
i = 1
soma = 0.0

while i <= n:
    num = 1
    j = 1
    while j <= i:
        num *= j
        j += 1

    den = 1
    k = 1
    impar = 1
    while k <= i:
        den *= impar
        impar += 2
        k += 1

    soma += num / den
    i += 1

print(f"Resultado da soma: {soma}")

# ---------- Exercício 14 ----------
n = int(input("Digite o valor de N: "))
i = 1
soma = 0.0

while i <= n:
    numerador = 2 * i
    denominador = 2 * i + 1
    soma += numerador / denominador
    i += 1

print(f"Resultado da soma: {soma}")

# ---------- Exercício 15 ----------
n = int(input("Digite um número inteiro positivo: "))
fatorial = 1
i = 1

while i <= n:
    fatorial *= i
    i += 1

print(f"{n}! = {fatorial}")

# ---------- Exercício 16 ----------
# loop 'do-while' não ensinado

# ---------- Exercício 17 ----------
n = int(input("Digite um número inteiro: "))
i = 1

print(f"Divisores de {n} são:")
while i <= n:
    if n % i == 0:
        print(i)
    i += 1

# ---------- Exercício 18 ----------
n = int(input("Digite um número menor que 46: "))
i = 0
a = 0
b = 1

while i < n:
    print(a)
    temp = a + b
    a = b
    b = temp
    i += 1
print()

# ---------- Exercício 19 ----------
senha = 0
while senha != 2002:
    senha = int(input("Digite a senha: "))
    if senha != 2002:
        print("Senha Invalida")
    else:
        print("Acesso Permitido")

# ---------- Exercício 20 ----------
# loop 'do-while' não ensinado

# ---------- Exercício 21 ----------
n = int(input("Digite um número: "))
i = 1
soma = 0

while i < n:
    if n % i == 0:
        soma += i
    i += 1

if soma == n:
    print(f"{n} é um número perfeito")
else:
    print(f"{n} não é um número perfeito")
