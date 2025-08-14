"""
Escreva um programa em Python que, para a quantidade de alunos
especificada, ccolete as notas de cada aluno e exiba um resumo da turma

O programa deve conter as seguintes funções:

- coletar_notas() - pede ao usuário para digitar uma série
de notas em uma única linha. O programa deve converter as notas para o tipo
numérico (float) e retorná-las em uma lista.

- preencher_turma(qtde_alunos) - solicita a quantidade de alunos e,
para cada aluno, chamar a função coletar_notas() para preencher uma
lista com as notas de cada aluno.

- calcular_media(aluno) - recebe uma lista de notas de um aluno
e retorna a média aritmética.

- resumo_turma(turma) - percorre a lista de alunos e,
para cada um, exibir as notas e a média, formatando a média
para duas casas decimais.
"""


def coletar_notas():
    notas = input().split()
    for i in range(len(notas)):
        notas[i] = float(notas[i])  # casting para float
    return notas


def preencher_turma(qtde_alunos):
    turma = []
    for i in range(qtde_alunos):
        print(f"{i+1}º aluno: ", end=" ")
        aluno = coletar_notas()
        turma.append(aluno)
    return turma


def calcular_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
    return soma / len(aluno)


def resumo_turma(turma):
    for aluno in turma:
        media = calcular_media(aluno)
        print(f"Notas: {aluno} | Média: {media:.2f}")


# Função para testar o programa
def main():
    qtde_alunos = int(input("Quantidade: "))
    turma = preencher_turma(qtde_alunos)
    resumo_turma(turma)


# Principal
main()
