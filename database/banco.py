import sqlite3

class Cadastrados():
    def __init__(self):
        self.conexao = sqlite3.connect('database/cadastrados.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                     idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                     usuario TEXT NOT NULL,
                     senha TEXT NOT NULL
                     )""")
        self.conexao.commit()
        c.close()

class Ficheiro():
    def __init__(self):
        self.conexao = sqlite3.connect('database/cadastrados.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS fichas(
                     idficha INTEGER PRIMARY KEY AUTOINCREMENT,
                     idusuario INTEGER,                    
                     nome TEXT NOT NULL,
                     idade INTEGER NOT NULL,
                     raca TEXT NOT NULL,
                     classe TEXT NOT NULL,
                     FOREIGN KEY (idusuario) REFERENCES usuarios(idusuario)
                     )""")
        self.conexao.commit()
        c.close()
