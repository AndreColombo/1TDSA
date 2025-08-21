"""
Dicionários

Criando um dicionário com informações sobre uma pessoa
Sintaxe:
nome = {'chave': 'valor'}
"""

pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
    }

# Imprimindo o dicionário - pessoa
print(pessoa)

# Acessando um valor utilizando a chave "nome"
print(f'\nNome: {pessoa["nome"]}')

# Adicionar uma nova informação - uma nov chave e um novo valor
pessoa["profissão"] = "Programador"
print(pessoa)

# Alterando um valor de uma chave
pessoa["idade"] = 31
print(f'Nova idade: {pessoa["idade"]}')

# Removendo um par de chaves do dicionário
del pessoa["cidade"]
print(pessoa)
