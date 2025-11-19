import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from key_manager import load_key, generate_key
from encryptor import encrypt_file, encrypt_folder
from decryptor import decrypt_file, decrypt_folder

class FileEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryptor")
        self.root.geometry("500x400")

        if not os.path.exists("secret.key"):
            generate_key()
            messagebox.showinfo("Ключ", "Ключ шифрования создан автоматически.")

        self.key = load_key()

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="File Encryptor", font=("Arial", 16))
        title_label.pack(pady=20)

        self.encrypt_file_btn = tk.Button(self.root, text="Зашифровать файл", command=self.encrypt_file_action)
        self.encrypt_file_btn.pack(pady=10)

        self.decrypt_file_btn = tk.Button(self.root, text="Расшифровать файл", command=self.decrypt_file_action)
        self.decrypt_file_btn.pack(pady=10)

        self.encrypt_folder_btn = tk.Button(self.root, text="Зашифровать папку", command=self.encrypt_folder_action)
        self.encrypt_folder_btn.pack(pady=10)

        self.decrypt_folder_btn = tk.Button(self.root, text="Расшифровать папку", command=self.decrypt_folder_action)
        self.decrypt_folder_btn.pack(pady=10)

        self.status = tk.Label(self.root, text="Готово", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def encrypt_file_action(self):
        filepath = filedialog.askopenfilename(title="Выберите файл для шифрования")
        if filepath:
            try:
                encrypt_file(filepath, self.key)
                self.status.config(text=f"Файл {filepath} зашифрован")
                messagebox.showinfo("Успех", f"Файл {filepath} зашифрован")
            except Exception as e:
                self.status.config(text="Ошибка при шифровании")
                messagebox.showerror("Ошибка", str(e))

    def decrypt_file_action(self):
        filepath = filedialog.askopenfilename(title="Выберите файл для расшифровки", filetypes=[("Encrypted Files", "*.encrypted")])
        if filepath:
            try:
                decrypt_file(filepath, self.key)
                self.status.config(text=f"Файл {filepath} расшифрован")
                messagebox.showinfo("Успех", f"Файл {filepath} расшифрован")
            except Exception as e:
                self.status.config(text="Ошибка при расшифровке")
                messagebox.showerror("Ошибка", str(e))

    def encrypt_folder_action(self):
        folderpath = filedialog.askdirectory(title="Выберите папку для шифрования")
        if folderpath:
            try:
                encrypt_folder(folderpath, self.key)
                self.status.config(text=f"Папка {folderpath} зашифрована")
                messagebox.showinfo("Успех", f"Папка {folderpath} зашифрована")
            except Exception as e:
                self.status.config(text="Ошибка при шифровании папки")
                messagebox.showerror("Ошибка", str(e))

    def decrypt_folder_action(self):
        folderpath = filedialog.askdirectory(title="Выберите папку для расшифровки")
        if folderpath:
            try:
                decrypt_folder(folderpath, self.key)
                self.status.config(text=f"Папка {folderpath} расшифрована")
                messagebox.showinfo("Успех", f"Папка {folderpath} расшифрована")
            except Exception as e:
                self.status.config(text="Ошибка при расшифровке папки")
                messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FileEncryptorApp(root)
    root.mainloop()