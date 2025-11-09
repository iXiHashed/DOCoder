import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def choose_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Выберите файл для шифрования/дешифровки")
    return file_path

def choose_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Выберите папку для шифрования/дешифровки")
    return folder_path

def show_message(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Информация", message)
    root.destroy()