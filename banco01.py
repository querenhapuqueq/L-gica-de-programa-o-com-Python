import sqlite3

class Backend():
    def conecta_banco(self):
        self.conexao = sqlite3.connect('Sistema_cadastro.bd')
        self.sql = self.conexao.cursor()
        print('Banco de dados ativado!')

    def desconecta_banco(self):
        self.conexao.close()
        print('Banco de dados finalizado!')

    def criar_tabela(self):
        self.conecta_banco()
        self.sql.execute('''
            CREATE TABLE IF NOT EXISTS
            usuarios (id INTERGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        senha TEXT NOT NULL,
                        confirmaSenha TEXT NOT NULL)
        
        ''')
        self.conexao.commit()
        print('Tabela criada com sucesso')
        self.desconecta_banco()


