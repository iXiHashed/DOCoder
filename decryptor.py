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

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.encrypted'):
                filepath = os.path.join(root, file)
                decrypt_file(filepath, key)
