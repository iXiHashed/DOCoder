from cryptography.fernet import Fernet

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    print(f"Файл {filename} зашифрован как {filename}.encrypted")