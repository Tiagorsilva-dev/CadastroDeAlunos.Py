import sqlite3
from tkinter import messagebox

class Sistema_De_Registro:
    def __init__(self):
        self.conn = sqlite3.connect('estudantes.bd')
        self.c = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.c.execute('''
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
        self.conn.commit()
    
    def register_student(self, estudante):
        self.c.execute(
            "INSERT INTO estudantes(nome, email, tel, sexo, data_de_nascimento, endereco, curso, picture) VALUES(?,?,?,?,?,?,?,?)",
            estudante
        )
        self.conn.commit()
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso")

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        for i in dados:
            print(f'ID: {i[0]} | Nome: {i[1]} | Email: {i[2]} | Telefone: {i[3]} | Sexo: {i[4]} | Data de Nascimento: {i[5]} | Endereço: {i[6]} | Curso: {i[7]} | Imagem: {i[8]}')

    def search_students(self, nome):
        self.c.execute("SELECT * FROM estudantes WHERE nome=?", (nome,))
        dados = self.c.fetchone()

        if dados:
            print(f'ID: {dados[0]} | Nome: {dados[1]} | Email: {dados[2]} | Telefone: {dados[3]} | Sexo: {dados[4]} | Data de Nascimento: {dados[5]} | Endereço: {dados[6]} | Curso: {dados[7]} | Imagem: {dados[8]}')
        else:
            print("Aluno não encontrado.")

    def update_students(self, novos_valores):
        query = """
        UPDATE estudantes 
        SET nome=?, email=?, tel=?, sexo=?, data_de_nascimento=?, endereco=?, curso=?, picture=? 
        WHERE id=?
        """
        self.c.execute(query, novos_valores)
        self.conn.commit()

        messagebox.showinfo("Sucesso", f"Aluno {novos_valores[0]} teve o cadastro atualizado com sucesso")

    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()

        messagebox.showinfo("Sucesso", f"Aluno com id {id} teve o cadastro excluído")


SistemaDeRegistro = Sistema_De_Registro()