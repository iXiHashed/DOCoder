import os
from key_manager import load_key, generate_key
from encryptor import encrypt_file
from decryptor import decrypt_file

def main():
    print("Добро пожаловать в DOCoder!")
    
    
    if not os.path.exists("secret.key"):
        print("Ключ не найден, генерируем новый...")
        generate_key()
        print("Ключ сгенерирован и сохранён как 'secret.key'")

    print("1. Зашифровать файл")
    print("2. Расшифровать файл")
    print("3. Зашифровать папку")
    print("4. Расшифровать папку")
    choice = input("Выберите действие (1, 2, 3 или 4): ")

    key = load_key()

    if choice == '1':
        filepath = choose_file()
        if filepath:
            encrypt_file(filepath, key)
            show_message(f"Файл {filepath} зашифрован.")
    elif choice == '2':
        filepath = choose_file()
        if filepath:
            decrypt_file(filepath, key)
            show_message(f"Файл {filepath} расшифрован.")
    elif choice == '3':
        folderpath = choose_folder()
        if folderpath:
            encrypt_folder(folderpath, key)
            show_message(f"Папка {folderpath} зашифрована.")
    elif choice == '4':
        folderpath = choose_folder()
        if folderpath:
            decrypt_folder(folderpath, key)
            show_message(f"Папка {folderpath} расшифрована.")
    else:
        print("Неверный выбор!")

if __name__ == "__main__":
    main()

