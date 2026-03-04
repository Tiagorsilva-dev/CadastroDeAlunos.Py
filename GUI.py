import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

def conectar():
    return sqlite3.connect("estudantes.bd")

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            tel TEXT NOT NULL,
            sexo TEXT NOT NULL,
            data_de_nascimento TEXT NOT NULL,
            endereco TEXT NOT NULL,
            curso TEXT NOT NULL,
            picture TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()


def cadastrar():
    conn = conectar()
    c = conn.cursor()

    c.execute("""
        INSERT INTO estudantes(nome,email,tel,sexo,data_de_nascimento,endereco,curso,picture)
        VALUES(?,?,?,?,?,?,?,?)
    """, (
        nome_var.get(),
        email_var.get(),
        tel_var.get(),
        sexo_var.get(),
        data_var.get(),
        endereco_var.get(),
        curso_var.get(),
        picture_var.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Aluno cadastrado!")
    limpar()
    listar()


def listar():
    for row in tree.get_children():
        tree.delete(row)

    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM estudantes")
    dados = c.fetchall()
    conn.close()

    for i in dados:
        tree.insert("", "end", values=i)


def deletar():
    item = tree.selection()
    if not item:
        return
    
    id = tree.item(item)['values'][0]

    conn = conectar()
    c = conn.cursor()
    c.execute("DELETE FROM estudantes WHERE id=?", (id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Aluno deletado!")
    listar()


def selecionar(event):
    item = tree.selection()
    if item:
        dados = tree.item(item)['values']
        nome_var.set(dados[1])
        email_var.set(dados[2])
        tel_var.set(dados[3])
        sexo_var.set(dados[4])
        data_var.set(dados[5])
        endereco_var.set(dados[6])
        curso_var.set(dados[7])
        picture_var.set(dados[8])


def atualizar():
    item = tree.selection()
    if not item:
        return

    id = tree.item(item)['values'][0]

    conn = conectar()
    c = conn.cursor()
    c.execute("""
        UPDATE estudantes
        SET nome=?, email=?, tel=?, sexo=?, data_de_nascimento=?, endereco=?, curso=?, picture=?
        WHERE id=?
    """, (
        nome_var.get(),
        email_var.get(),
        tel_var.get(),
        sexo_var.get(),
        data_var.get(),
        endereco_var.get(),
        curso_var.get(),
        picture_var.get(),
        id
    ))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Aluno atualizado!")
    listar()


def limpar():
    nome_var.set("")
    email_var.set("")
    tel_var.set("")
    sexo_var.set("")
    data_var.set("")
    endereco_var.set("")
    curso_var.set("")
    picture_var.set("")



root = tk.Tk()
root.title("Sistema de Registro Escolar")
root.geometry("1200x650")
root.configure(bg="#1e1e2f")

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                background="#2b2b3c",
                foreground="white",
                rowheight=25,
                fieldbackground="#2b2b3c")

style.map("Treeview",
          background=[("selected", "#4CAF50")])

nome_var = tk.StringVar()
email_var = tk.StringVar()
tel_var = tk.StringVar()
sexo_var = tk.StringVar()
data_var = tk.StringVar()
endereco_var = tk.StringVar()
curso_var = tk.StringVar()
picture_var = tk.StringVar()


frame_form = tk.Frame(root, bg="#1e1e2f")
frame_form.pack(pady=20)

def criar_label(texto, row, col):
    tk.Label(frame_form, text=texto, fg="white", bg="#1e1e2f",
             font=("Segoe UI", 9)).grid(row=row, column=col, padx=5, pady=5)

def criar_entry(var, row, col):
    tk.Entry(frame_form, textvariable=var, bg="#2b2b3c",
             fg="white", insertbackground="white",
             relief="flat", width=22).grid(row=row, column=col, padx=5)

campos = [
    ("Nome", nome_var),
    ("Email", email_var),
    ("Telefone", tel_var),
    ("Sexo", sexo_var),
    ("Data Nasc.", data_var),
    ("Endereço", endereco_var),
    ("Curso", curso_var),
    ("Picture", picture_var)
]

for i, (label, var) in enumerate(campos):
    linha = i // 4
    coluna = (i % 4) * 2
    criar_label(label, linha, coluna)
    criar_entry(var, linha, coluna + 1)


frame_btn = tk.Frame(root, bg="#1e1e2f")
frame_btn.pack(pady=15)

def botao(texto, cor, comando):
    tk.Button(frame_btn,
              text=texto,
              bg=cor,
              fg="white",
              activebackground=cor,
              relief="flat",
              width=15,
              height=2,
              command=comando).pack(side="left", padx=8)

botao("Cadastrar", "#4CAF50", cadastrar)
botao("Atualizar", "#2196F3", atualizar)
botao("Deletar", "#f44336", deletar)
botao("Limpar", "#9E9E9E", limpar)

colunas = ("ID","Nome","Email","Tel","Sexo","Data","Endereço","Curso","Picture")

tree = ttk.Treeview(root, columns=colunas, show="headings", height=18)

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=130)

tree.pack(fill="both", expand=True, padx=20, pady=10)
tree.bind("<<TreeviewSelect>>", selecionar)

listar()

root.mainloop()


frame_btn = tk.Frame(root, bg="#f4f6f9")
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Cadastrar", bg="#4CAF50", fg="white", width=15, command=cadastrar).pack(side="left", padx=5)
tk.Button(frame_btn, text="Atualizar", bg="#2196F3", fg="white", width=15, command=atualizar).pack(side="left", padx=5)
tk.Button(frame_btn, text="Deletar", bg="#f44336", fg="white", width=15, command=deletar).pack(side="left", padx=5)
tk.Button(frame_btn, text="Limpar", bg="#9E9E9E", fg="white", width=15, command=limpar).pack(side="left", padx=5)


colunas = ("ID","Nome","Email","Tel","Sexo","Data","Endereço","Curso","Picture")

tree = ttk.Treeview(root, columns=colunas, show="headings", height=15)

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(fill="both", expand=True)
tree.bind("<<TreeviewSelect>>", selecionar)

listar()

root.mainloop()