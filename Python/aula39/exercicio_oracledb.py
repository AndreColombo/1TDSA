import oracledb


def get_conexao():
    try:
        conn = oracledb.connect(
            user="rm563112",
            password="180507",
            host="oracle.fiap.com.br",
            port="1521",
            service_name="orcl",
        )
        print("\nConexão com Oracle DB realizada!")
    except Exception as e:
        print(f"\nErro ao obter a conexão: {e}")
    return conn


def criar_tabela(conn):
    cursor = conn.cursor()
    try:
        sql = """
            CREATE TABLE produto (
                id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                nome VARCHAR2(50),
                descricao VARCHAR2(150),
                fornecedor VARCHAR2(50),
                preco NUMBER(10, 2)
            )
        """
        cursor.execute(sql)
        print(f"Tabela PRODUTO criada com sucesso!")
    except oracledb.Error as e:
        print(f"\nErro de conexão: {e}")


def inserir_produto(nome, descricao, fornecedor, preco):
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO produto (nome, descricao, fornecedor, preco)
            VALUES (:nome, :descricao, :fornecedor, :preco)
        """
        cursor.execute(
            sql,
            {
                "nome": nome,
                "descricao": descricao,
                "fornecedor": fornecedor,
                "preco": preco,
            },
        )
        conn.commit()
        print(f"Produto {nome} inserido com sucesso!")
    except Exception as e:
        print(f"\nErro ao inserir produto: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()


def listar_produtos():
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM produto"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(
                f"ID: {row[0]} | Nome: {row[1]} | Descrição: {row[2]} | Fornecedor: {row[3]} | Preço: {row[4]}"
            )
    except Exception as e:
        print(f"\nErro ao listar a tabela produto: {e}")
    finally:
        if conn:
            conn.close()


def buscar_produto_por_id(id):
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM produto WHERE id = :id"
        cursor.execute(sql, {"id": id})
        produto = cursor.fetchone()
        print(f"{produto}")
    except Exception as e:
        print(f"\nErro ao buscar produto na tabela: {e}")
    finally:
        if conn:
            conn.close()


def atualizar_preco_produto(id, novo_preco):
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "UPDATE produto SET preco = :novo_preco WHERE id = :id"
        cursor.execute(sql, {"id": id, "novo_preco": novo_preco})
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Preço do produto alterado com sucesso")
        else:
            print(f"Nenhum produto com ID {id} econtrado!")
    except Exception as e:
        print(f"\nErro ao atualizar produto na tabela: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()


def deletar_produto(id):
    conn = get_conexao()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM produto WHERE id = :id"
        cursor.execute(sql, {"id": id})
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Produto deletado com sucesso")
        else:
            print(f"Nenhum produto com ID {id} econtrado!")
    except Exception as e:
        print(f"\nErro ao deletar produto na tabela: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()


def menu():
    print("\n*** MENU PRINCIPAL ***")
    while True:
        print("\n1. Inserir produto")
        print("2. Listar produtos")
        print("3. Buscar produto por ID")
        print("4. Atualizar preço do produto")
        print("5. Deletar produto")
        print("6. Sair")

        escolha = int(input("Escolha uma opção: "))

        match escolha:
            case 1:
                nome = input("Insira o nome do produto: ")
                descricao = input("Insira a descrição do produto: ")
                fornecedor = input("Insira o fornecedor do produto: ")
                preco = float(input("Insira o preço do produto: "))
                inserir_produto(nome, descricao, fornecedor, preco)
            case 2:
                listar_produtos()
            case 3:
                id = int(input("Digite o ID do produto que deseja buscar: "))
                buscar_produto_por_id(id)
            case 4:
                id = int(input("Digite o ID do produto que deseja atualizar: "))
                novo_preco = int(input("Digite o novo preço do produto escolhido: "))
                atualizar_preco_produto(id, novo_preco)
            case 5:
                id = int(input("Digite o ID do produto que deseja deletar: "))
                deletar_produto(id)
            case 6:
                print("Saindo do programa")
                break
            case _:
                print("Opção inválida, tente novamente.")


# conn = get_conexao()
# criar_tabela(conn)
menu()
