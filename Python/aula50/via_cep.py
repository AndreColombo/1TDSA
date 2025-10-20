import requests
import json


def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    print(f"Buscando endereço para o CEP: {cep}")

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

    if response.status_code == 200:
        dados_endereco = response.json()
        print("\n--- Endereço encontrado! ---")
        if "erro" not in dados_endereco:
            print(f"CEP: {dados_endereco.get('cep')}")
            print(f'Logradouro: {dados_endereco.get("logradouro")}')
            print(f'Bairro: {dados_endereco.get("bairro")}')
            print(
                f'Cidade/UF: {dados_endereco.get("localidade")}/{dados_endereco.get("uf")}'
            )
        else:
            print(f"Erro: O CEP {cep} não foi encontrado!")
    else:
        print(f"\nErro ao buscar o CEP {cep}. Status code: {response.status_code}")
        print("Verifique se o CEP foi digitado corretamente!")


# Programa Principal
cep = input("CEP: ")
consultar_cep(cep)
