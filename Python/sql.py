import mysql.connector
from mysql.connector import Error

def criar_tabela():
    
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='nome_do_banco',
            user='seu_usuario',
            password='sua_senha'
        )
        
        if conexao.is_connected():
            print("Conexão bem-sucedida ao banco de dados")

            comando_sql = """
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                idade INT NOT NULL
            );
            """

            cursor = conexao.cursor()
            cursor.execute(comando_sql)

            print("Tabela 'clientes' criada ou já existente.")
    
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão fechada.")

criar_tabela()