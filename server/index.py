from flask import Flask, render_template, request, redirect, url_for

 

app = Flask(__name__)

 

# Simulando uma lista de usuários com nomes de usuário e senhas

users = {'user1': 'password1', 'user2': 'password2'}

 

@app.route('/')

def home():

    return render_template('login.html')

 

@app.route('/login', methods=['POST'])

def login():

    username = request.form['username']

    password = request.form['password']

 

    # Verifica se o nome de usuário e senha correspondem

    if username in users and users[username] == password:

        return 'Login bem-sucedido!'

    else:

        return 'Credenciais inválidas. Tente novamente.'

 

if __name__ == '__main__':

    app.run(debug=True)