import sqlite3
from tkinter import messagebox

class Sistema_De_Registro:
    def __init__(self):
        self.conn = sqlite3.connect('estudantes.bd')
        self.c = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       email TEXT NOT NULL,
                       tel TEXT NOT NULL,
                       sexo TEXT NOT NULL,
                       data_de_nascimento TEXT NOT NULL,
                       endereco TEXT NOT NULL,
                       curso TEXT NOT NULL,
                       picture TEXT NOT NULL)''')
    
    def register_student(self, estudantes,):
        self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_de_nascimento, endereco, curso, picture) VALUES(?,?,?,?,?,?,?,?)", (estudantes))
        self.conn.commit()

        messagebox.showinfo("Aluno cadstrado com sucesso")

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        for i in dados:
            print(f'ID: {i[0]} | Nome: {i[1]} | Email :{i[2]} | Telefone : {i[3]} | Sexo :{i[4]} | Date de Nascimento: {i[5]} | Endereco :{i[6]} | Curso :{i[7]} | Imagem :{i[8]}')

    def search_students(self, nome):
        self.c.execute("SELECT * FROM estudantes WHERE id=?",(id,))
        dados=self.c.fetchone()
        
        print(f'ID: {dados[0]} | Nome: {dados[1]} | Email :{dados[2]} | Telefone : {dados[3]} | Sexo :{dados[4]} | Date de Nascimento: {dados[5]} | Endereco :{dados[6]} | Curso :{dados[7]} | Imagem :{dados[8]}')

    def update_students(self, novos_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_de_nascimento=?, endereco=?, curso=?, picture=? WHERE id = ?"
        self.c.execute(query,novos_valores)
        self.conn.commit()

        messagebox.showinfo("Aluno {} teve o cadastro atualizado com sucesso".format(novos_valores[0]))

    def delete_studet(self, id):
        self.c.execute("DELETE FROM estudantes WHRERE id=?", (id,))
        self.conn.commit

        messagebox.showinfo("Aluno com id {} teve o cadastro atualizado com sucesso".format(id))


SistemaDeRegistro = Sistema_De_Registro()