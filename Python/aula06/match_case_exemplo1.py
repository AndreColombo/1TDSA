linguagem = input("Digite uma linguagem: ").lower()
match linguagem:
    case "javascript":
        print("Desenvolvedor Web")
    case "python":
        print("Cientista de Dados")
    case "php":
        print("Desenvolvedor Back-end")
    case "solidity":
        print("Desenvolvedor Blockchain")
    case "java":
        print("Desenvolvedor Mobile ou Back-end")
    case _:
        print("Linguagem não encontrada!")
