import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

# Criando a janela do app
janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.configure(bg="#F0F0F0")
janela.geometry("500x500")

# Cabeçalho da janela
fonte_cabecalho = font.Font(family="Arial", size=24, weight="bold")
titulo_cabelaho = tk.Label(janela, text="Lista de Tarefas", font=fonte_cabecalho, bg="#F0F0F0", fg="#333").pack(pady=20)


# Loop principal do app
janela.mainloop()