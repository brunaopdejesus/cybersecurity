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
