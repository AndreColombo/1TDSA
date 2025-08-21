try:
    arquivo = open("meu_arquivo.txt", "w")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
except Exception as e:
    print(f"Erro: {e}")
else:
    print("O arquivo foi lido com sucesso!")
finally:
    arquivo.close()
    print("Arquivo fechado!")
