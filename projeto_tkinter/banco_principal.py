import sqlite3
from sqlite3 import Error

# --------------------- Classe Banco de dados ----------------------
class Banco():
    def conecta_banco(self):
        self.conexao = sqlite3.connect('bancodedados.bd')
        self.sql = self.conexao.cursor()
        print('Banco de dados ativado!')

    def desconecta_banco(self):
        self.conexao.close()
        print('Banco de dados desconectado!')

    def criar_tabela(self):
        self.conecta_banco()
        try:
            self.sql.execute('''
                CREATE TABLE IF NOT EXISTS 
                produto (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome_produto VARCHAR(30) NOT NULL,
                          preco_produto DOUBLE NOT NULL)     
            ''')
            self.conexao.commit()
            print('Tabela criada com sucesso!')
            self.desconecta_banco()
        except Error:
            print('Ocorreu erro!', Error)
