from flask import Flask, redirect, render_template, request, url_for
import cx_Oracle

# Configurar o aplicativo Flask
app = Flask(__name__)

# Configurar a conexão com o banco de dados Oracle
oracle_connection = cx_Oracle.connect("rm99518/090505/ORACLE.FIAP.COM.BR/ORCL")

@app.route("/teste")
def ola():
    return 'Olá Mundo!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logar', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        
        # Exemplo de consulta ao banco de dados
        cursor = oracle_connection.cursor()
        cursor.execute("SELECT * FROM sua_tabela WHERE nome = :1 AND senha = :2", (nome, senha))
        resultado = cursor.fetchall()
        
        if resultado:
            # Autenticação bem-sucedida, você pode redirecionar para uma página de sucesso
            return redirect(url_for('pagina_de_sucesso'))
        else:
            # Autenticação falhou, você pode redirecionar para uma página de erro
            return redirect(url_for('pagina_de_erro'))

@app.route('/pagina_de_sucesso')
def pagina_de_sucesso():
    return 'Autenticação bem-sucedida!'

@app.route('/pagina_de_erro')
def pagina_de_erro():
    return 'Autenticação falhou!'

if __name__ == "__main__":
    app.run()
