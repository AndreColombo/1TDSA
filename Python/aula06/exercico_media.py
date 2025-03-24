"""
if-elif-else:
Escreva um programa em Python que leia o nome de um aluno e as 3 notas obtidas em uma disciplina. O programa deve calcular a média das 3 notas e definir o status (aprovado (>=6) ou reprovado). Além disso, o programa deve definir o conceito de acordo com a média:

match-case:
- conceito "B" (média >= 8 e média <= 9)
- conceito "A" (média >= 9 e média < 10)
- conceito "c" (média >= 7 e média < 8)
- conceito "D" (média >= 6 e média < 7)
- conceito "E" (média < 6)
"""

nomeAluno = input("Digite o nome do aluno: ")
disciplina = input("Digite o nome da disciplina: ")
print("-------------------------")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
conceito = ""

if media >= 9 and media <= 10:
    conceito = "A"
elif media >= 8 and media < 9:
    conceito = "B"
elif media >= 7 and media < 8:
    conceito = "C"
elif media >= 6 and media < 7:
    conceito = "D"
else:
    conceito = "E"

print("-------------------------")

match conceito:
    case "A":
        print(
            f'{nomeAluno} está aprovado na disciplina {disciplina}, com conceito "A" e média {media:.1f}'
        )
    case "B":
        print(
            f'{nomeAluno} está aprovado na disciplina {disciplina}, com conceito "B" e média {media:.1f}'
        )
    case "C":
        print(
            f'{nomeAluno} está aprovado na disciplina {disciplina}, com conceito "C" e média {media:.1f}'
        )
    case "D":
        print(
            f'{nomeAluno} está aprovado na disciplina {disciplina}, com conceito "D" e média {media:.1f}'
        )
    case "E":
        print(
            f'{nomeAluno} está reprovado na disciplina {disciplina}, com conceito "E" e média {media:.1f}'
        )
    case _:
        print("Conceito não encontrado")

print("-------------------------")
