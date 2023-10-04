import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\logonrmlocal\Downloads\instantclient_21_11")

# Substitua 'seu_usuario' e 'sua_senha' pelas credenciais do seu banco de dados Oracle
dsn_tns = cx_Oracle.makedsn('ORACLE.FIAP.COM.BR', '1521', 'ORCL')
conn = cx_Oracle.connect(user='rm99518', password='090505', dsn=dsn_tns)

def realizar_login(nome, senha):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = :1 AND senha = :2", (nome, senha))
    result = cursor.fetchone()
    print(result)
    cursor.close()
    return result

# realizar_login('carlos@example.com', 'senhaabc')