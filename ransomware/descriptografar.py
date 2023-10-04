import os
from Crypto.Cipher import AES

def decrypt_file(key, file_path):
    with open(file_path, 'rb') as file_encrypted:
        encrypted_data = file_encrypted.read()
        
        # O IV (nonce) é o primeiro bloco de 16 bytes
        iv = encrypted_data[:16]
        
        # O texto cifrado vem após o IV
        ciphertext = encrypted_data[16:-16]
        
        # A tag GCM é o último bloco de 16 bytes
        tag = encrypted_data[-16:]
        
        # Criar um objeto de cifra AES em modo GCM
        cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
        
        # Descriptografar o texto cifrado
        plaintext = cipher.decrypt(ciphertext)
        
        # Verificar a tag GCM para autenticidade
        try:
            cipher.verify(tag)
        except ValueError:
            raise ValueError("Autenticação falhou. A chave ou o arquivo podem estar incorretos.")
    
    # Escrever o arquivo descriptografado
    with open(file_path[:-4], 'wb') as file:
        file.write(plaintext)

def decrypt_folder(key, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(key, file_path)
            os.remove(file_path)  # Remove o arquivo criptografado

if __name__ == '__main__':
    key = b'ChaveAESDe256Bits'  # Substitua pela chave correta que foi usada para criptografar
    folder_to_decrypt = 'C:\\Users\\logonrmlocal\\Documents\\pasta_test'  # Pasta que você deseja descriptografar

    decrypt_folder(key, folder_to_decrypt)
