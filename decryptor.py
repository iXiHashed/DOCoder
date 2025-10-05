from cryptography.fernet import Fernet

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    output_filename = filename.replace(".encrypted", "") + ".decrypted"
    with open(output_filename, "wb") as file:
        file.write(decrypted_data)
    print(f"Файл {filename} расшифрован как {output_filename}")