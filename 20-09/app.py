from flask import Flask, redirect, render_template, request
import banco

app = Flask(__name__)

@app.route("/teste")
def ola():
    return 'Olá Mundo!'

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/logar', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         nome = request.form['nome']
#         senha = request.form['senha']
        
#         # Verifica as credenciais utilizando a função do banco.py
#         result = banco.realizar_login(nome, senha)
        
#         if result:
#             # Credenciais corretas, redireciona para alguma página de sucesso
#             return redirect('http://www.google.com.br')
#         else:
#             # Credenciais incorretas, você pode redirecionar para uma página de erro
#             return redirect('/')
    
#     if request.method == 'GET':
#         # Lógica para lidar com solicitações GET, como exibir um formulário de login
#         return render_template('login.html')  # Substitua por seu template de login

@app.route('/logar', methods=['POST', 'GET'])
def login():

    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        try:
            print(f"SELECT * FROM usuarios WHERE email = '{nome}' AND senha = '{senha}'")
            cursor.execute(f"SELECT * FROM usuarios WHERE email = '{nome}' AND senha = '{senha}'")
            for row in cursor:
                print(row[1])
                if(row[1] != ""):
                    return redirect('/noticias')
                else:
                    return redirect('/logar')
        except Exception as e:
            print('Erro: ', e)
            return redirect('/logar')

@app.route('/noticias')
def noticias():
    try:
        cursor.execute(f"SELECT * FROM comentarios")
        print(cursor)
        conteudo = ""
        for row in cursor:
            conteudo += row[1]
    except Exception as e:

        print('Erro: ',  e)
    return render_template('noticias.html', content = conteudo)

# @app.route('/comentar', methods = ['POST'])
# def comentar():
#     comentario = request.form['comentario']
#     try:
#         cursor.execute(f"INSERT INTO COMENTARIOS (COMENTARIO) VALUES ('{comentario}')")
#         conn.commit()

# if __name__ == "__main__":
#     app.run()
