import itertools

# Define o número de letras das senhas
num_letras = 3

# Define o conjunto de caracteres que serão usados para gerar as senhas
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Gera todas as combinações possíveis de caracteres com o tamanho especificado
combinacoes = itertools.product(caracteres, repeat=num_letras)

# Abre o arquivo para salvar as senhas
with open('senhas.txt', 'w') as f:
    # Escreve cada combinação no arquivo em uma linha separada
    for combinacao in combinacoes:
        senha = ''.join(combinacao)
        f.write(senha + '\n')

print('Lista de senhas gerada com sucesso!')
