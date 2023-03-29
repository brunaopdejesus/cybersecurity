import PyPDF2

# Abre o arquivo PDF protegido por senha
pdf_reader = PyPDF2.PdfReader(open('teste2_protected.pdf', 'rb'))

# Abre o arquivo de texto com as senhas
with open('senhas.txt', 'r') as f:
    # Loop através de cada senha na lista
    for senha in f:
        senha = senha.strip() # Remove qualquer espaço em branco no início ou no final da senha
        # Tenta desbloquear o arquivo PDF com a senha atual
        print(pdf_reader.decrypt(senha))
        if pdf_reader.decrypt(senha) == 2:
            print('Arquivo PDF desbloqueado com a senha:', senha)
            break # Para a execução se a senha correta for encontrada
        else:
            print('Senha incorreta:', senha)
