"""
Manipulação de dados em Arquivos texto
Pensamento Computacional

- Decomposição em 3 etapas:
 1. Abertura do Arquivo
 2. Processamento de dados (escrever e ler)
 3. Fechamento do Arquivo

Em python, essas operações ocorrem através de duas funções
 - open() - lida com a etapa 1
   Modos de operação:
      - "w" (write - escrita) - cria um arquivo novo, permitindo a escrita...
      Obs.: se o arquivo já existir, todo o seu conteúdo será APAGADO e um novo arquivo será criado.
      - "r" (read - leitura) - abre o arquivo já existente APENAS para leitura.
      - "a" (append - adicionar) - abre o arquivo para escrita, adicionando um novo item (elemento) ao final do arquivo.
      - abertura com with - permite que o arquivo seja automaticamente fechado, ao término da operação.
 - .close() - método que fecha o arquivo - lida com a etapa 3
"""

# Exemplo prático de persistência de dados em Arquivos Texto
import os

"""
Escrever uma lista de strings (nome de alunos) em um arquivo
Sobrescrever os dados existentes ("w")
"""
ARQUIVO_TEXTO = "cadastro.txt"


def escrever(dados):
    print(">>> Escrevendo no Arquivo...")

    try:
        """
        with permite que o arquivo seja fechado através da abstração,
        escondendo a complexidade do gerenciamento de recursos
        """
        with open(ARQUIVO_TEXTO, "w") as arquivo:
            for item in dados:
                arquivo.write(f"{item}\n")
        print(f"\n[SUCESSO] Dados escritos em {ARQUIVO_TEXTO}")
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro ao escrever no arquivo: {e}")


"""
Leitura de todas as linhas de um arquivo, retornando como uma lista
"""


def ler():
    print("<<< Lendo dados do Arquivo...")
    try:
        with open(ARQUIVO_TEXTO, "r") as arquivo:
            linhas = []
            for linha in arquivo.readlines():
                # removve os espaçoes em branco e quabra linhas
                linhas.append(linha.strip())
            return linhas
    except FileNotFoundError:
        return []
    except Exception as e:
        print("\n[ERRO] Ocorreu um erro ao ler o arquivo: {e}")
        return []


"""
Adicionar uma nova string ao final do arquivo
"""


def adicionar(novo_dado):
    print(">>> Adicionando um novo dado ao final do arquivo...")
    try:
        with open(ARQUIVO_TEXTO, "a") as arquivo:
            arquivo.write(f"{novo_dado}\n")
        print(f"\n[SUCESSO] {novo_dado} foi inserido no ARQUIVO!")
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro ao adicionar {novo_dado} no arquivo: {e}")


"""
Exibe o menu de opções para o usuário e processa as informações
"""


def menu():
    print(">>> Menu de Operações <<<")
    while True:
        print("\n --- Persistência de Dados em Arquivos ---")
        print("1. Escrever no arquivo")
        print("2. Ler do arquivo")
        print("3. Adicionar no arquivo")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            dados_brutos = input(
                "Digite os dados separados por vírgula (Ex. Ana, Bruno, Carlos): "
            )
            dados = dados_brutos.split(",")
            dados_limpos = []
            for item in dados:
                dados_limpos.append(item.strip())
            escrever(dados_limpos)
        elif escolha == "2":
            dados = ler()

            if dados:
                for item in dados:
                    print(item)
                else:
                    print("\nO arquivo está vazio ou não existe!")
        elif escolha == "3":
            novo_dado = input("Digite o novo dado: ")
            adicionar(novo_dado)
        elif escolha == "4":
            print("Saindo do programa... até breve!")
            break
        else:
            print("\nOpção inválida. Escolha uma opção (1-4)")


# Programa principal
menu()
