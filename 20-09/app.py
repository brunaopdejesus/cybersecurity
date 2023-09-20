from flask import Flask, redirect, render_template, request
import banco

app = Flask(__name__)

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
        
        # Verifica as credenciais utilizando a função do banco.py
        result = banco.realizar_login(nome, senha)
        
        if result:
            # Credenciais corretas, redireciona para alguma página de sucesso
            return redirect('http://www.google.com.br')
        else:
            # Credenciais incorretas, você pode redirecionar para uma página de erro
            return redirect('/')
    
    if request.method == 'GET':
        # Lógica para lidar com solicitações GET, como exibir um formulário de login
        return render_template('login.html')  # Substitua por seu template de login

if __name__ == "__main__":
    app.run()
