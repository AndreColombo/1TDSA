import requests
import oracledb

# André Colombo - rm563112
# José Diogo - rm562341

def get_connection():
    try:
        conn = oracledb.connect(
            user="rm563112",
            password="180507",
            host="oracle.fiap.com.br",
            port="1521",
            service_name="orcl"
        )
        print("Conexão com Oracle DB realizada!")
    except Exception as e:
        print(f"Erro ao obter a conexão: {e}")
    return conn

def inserir(name, temp, temp_min, temp_max):
    print("\n--- Inserindo cidade na tabela ---")
    conn = get_connection()

    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO temp_cidade (name, temp, temp_min, temp_max)
            VALUES (:name, :temp, :temp_min, :temp_max)
        """
        cursor.execute(
            sql,
            {
                "name": name,
                "temp": temp,
                "temp_min": temp_min,
                "temp_max": temp_max,
            },
        )
        conn.commit()
        print(f"\nCidade {name} adicionada com sucesso!")
    except oracledb.Error as e:
        print(f"\nErro ao inserir cidade: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

def consultar_cidade(cidade):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=0bb4ab5f1e70e19db0dc58428460bf99&units=metric&lang=pt_br"

    print(f"Buscando temperatura da cidade: {cidade}")

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

    if response.status_code == 200:
        dados_cidade = response.json()
        print("\n--- Clima encontrado! ---")
        if "erro" not in dados_cidade:
            name, temp, temp_min, temp_max = dados_cidade.get('name'), dados_cidade.get('main').get('temp'), dados_cidade.get('main').get('temp_min'), dados_cidade.get('main').get('temp_max')
            print(f'Cidade: {name} \nTemperatura Atual: {temp} \nTemperatura Mínima: {temp_min} \nTemperatura Máxima: {temp_max}')
            return name, temp, temp_min, temp_max
        else:
            print(f"Erro: A cidade {cidade} não foi encontrado!")
    else:
        print(f"\nErro ao buscar a cidade {cidade}. Status code: {response.status_code}")
        print("Verifique se o nome da cidade foi digitado corretamente!")


def main():
    while True:
        escolha = int(input("Procurar nova cidade? \n1. Sim \n2. Não \nR: "))
        match escolha:
            case 1:
                cidade = input("\nDigite o nome da Cidade: ")
                name, temp, temp_min, temp_max = consultar_cidade(cidade)
                inserir(name, temp, temp_min, temp_max)
            case 2:
                return False

# Programa Principal
main()