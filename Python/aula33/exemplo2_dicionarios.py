"""
Principais métodos (mais comuns)
- keys(): Retorna uma "visão" de todas as chaves do dicionário
- values(): Retorna uma "visão" de todos os valores do dicionário
- items(): Retorna uma "visão" dos pares de chave-valor como tupla
- get(): Acessa o valor de forma segura (retornando uma valor padrão)
"""

carro = {
    "marca": "Jeep",
    "modelo": "Compass",
    "ano": 2025
    }

# Iterando sobre as chaves
for chave in carro.keys():
    print(chave)

# Iterando sobre os valores
for valor in carro.values():
    print(valor)

# Iterando sobre os pares de chave-valor - método items()
for chave, valor in carro.items():
    print(f"{chave}: {valor}")

# Acesso ao dicionário com chave inexistente
# print(carro["cor"])

# Acesso a um elemento do dicionário com o método get() - evitar erros
cor = carro.get("cor", "Não especificado!")
print(f"Cor: {cor}")
print(f"Marca: {carro.get('marca')}")
