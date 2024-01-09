'''import customtkinter
from banco_principal import Banco
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

class ModeloTelaPrincipal(Banco):
    def __init__(self, windows):
        self.janela = windows
        self.janela.title('Cadastro de Produtos')
        self.janela.geometry('600x600+450+0')
        self.janela._set_appearance_mode('light')
        self.criar_tabela()

        #--------------------- Título ---------
        self.titulo = customtkinter.CTkLabel(self.janela,
                                             text='Cadastrar nomes dos Produtos',
                                             font=('Poppins Bold', 25, 'bold'),
                                             text_color='black')
        self.titulo.pack()
        #---------------------- Labels e caixas de textos --------------------
        self.label_produto = customtkinter.CTkLabel(self.janela,
                                                    text='produto',
                                                    font=('Courier', 25, 'bold'))
        self.label_produto.place(x=10, y=100)

        self.caixa_produto = customtkinter.CTkEntry(self.janela,
                                                    placeholder_text='Nome do Produto',
                                                    width=300, height=30,
                                                    fg_color='#d9d9d9')
        self.caixa_produto.place(x=150, y= 100)

        self.preco = customtkinter.CTkLabel(self.janela,
                                           text='Preço',
                                           font=('Courier', 25, 'bold'))
        self.preco.place(x=10, y=150)
        self.caixa_preco = customtkinter.CTkEntry(self.janela,
                                                 placeholder_text='Valor do produto',
                                                 width=300, height=30,
                                                 fg_color='#d9d9d9')
        self.caixa_preco.place(x=150, y=150)
        # -----------------------------BOTÕES-------------------------------------------

        self.botao_cadastrar = customtkinter.CTkButton(self.janela,
                                                       text='Cadastrar',
                                                       command=self.cadastrar)
        self.botao_cadastrar.place(x=10, y=250)

        self.botao_atualizar = customtkinter.CTkButton(self.janela,
                                                       text='Atualizar',
                                                       command=self.atualizar_dados)
        self.botao_atualizar .place(x=200, y=250)

        self.botao_deletar= customtkinter.CTkButton(self.janela,
                                                    text='Deletar',
                                                    command=self.deletar_dados)
        self.botao_deletar.place(x=400, y=250)

        # -------------- CRIANDO UMA VISUALIZAÇÃO DE DADOS  -------------------

        self.relatorio = ttk.Treeview(self.janela,
                                      columns=('id', 'nome_produto', 'preco_produto'),
                                      show='headings')
        self.relatorio.column('id', minwidth=50, width=100)
        self.relatorio.column('nome_produto', minwidth=50, width=100)
        self.relatorio.column('preco_produto', minwidth=50, width=100)

        self.relatorio.heading('id', text='ID')
        self.relatorio.heading('nome_produto', text='PRODUTO')
        self.relatorio.heading('preco_produto', text='PREÇO')
        self.relatorio.place(x=20, y=300)
        self.mostrar_dados()

        self.relatorio.bind('<Double-1>', self.multiplo_clique)



        # -------------- PESQUISANDO DADOS  -------------------

        self.label_pesquisa = customtkinter.CTkLabel(self.janela,
                                                     text= 'Nome para a pesquisa',
                                                     font=('Courier', 20, 'bold'))
        self.label_pesquisa.place(x=20, y=550)

        self.caixa_pesquisa = customtkinter.CTkEntry(self.janela)
        self.caixa_pesquisa.place(x=300, y=550)
        self.botao_pesquisa = customtkinter.CTkButton(self.janela,
                                                      text='Pesquisar',
                                                      command=self.pesquisar_dados)
        self.botao_pesquisa.place(x=450, y=550)

        self.voltar = customtkinter.CTkButton(self.janela,
                                              text='Lista completa',
                                              command=self.mostrar_dados)
        self.voltar.place(x=450, y=300)


    def cadastrar(self):
        self.capturar_nome = self.caixa_produto.get()
        self.capturar_preco = self.caixa_preco.get()
        self.conecta_banco()
        self.sql.execute('''
                INSERT INTO  produto (nome_produto, preco_produto)
                values (?,?)
                ''', (self.capturar_nome, self.capturar_preco))
        try:
            if self.capturar_nome == '' or self.capturar_preco == '':
                messagebox.showerror('sistema de cadastro', 'Preencha todos os campos')
            else:
                self.conexao.commit()
                messagebox.showinfo('Cadastro', f'Parabéns! Dados salvos!')
                self.mostrar_dados()
                self.desconecta_banco()
                self.limpar_dados()

        except:
            messagebox.showerror('Cadastro', 'Erro no processamento do seu cadastro.')
            self.desconecta_banco()
        self.desconecta_banco()

    def limpar_dados(self):
        self.caixa_produto.delete(0, 'end')
        self.caixa_preco.delete(0, 'end')

    def mostrar_dados(self):
        self.relatorio.delete(*self.relatorio.get_children())
        self.conecta_banco()
        self.sql.execute('''SELECT * FROM produto ORDER BY id''')
        self.lista_dados = self.sql.fetchall()
        for item in self.lista_dados:
            self.relatorio.insert('', 'end', values=(item))

    def deletar_dados(self):
        try:
            self.conecta_banco()
            self.selecionar = self.relatorio.item(self.relatorio.selection()[0],'values')
            self.sql.execute('''DELETE FROM produto WHERE id= ''' + self.selecionar[0])
            self.conexao.commit()

            messagebox.showinfo('Exclusão', 'Dados removidos com sucesso!')
            self.mostrar_dados()
            self.desconecta_banco()
        except IndexError:
            messagebox.showerror('Exclusão','Selecione um dado para excluir')
            self.desconecta_banco()

    def atualizar_dados(self):
        try:
            self.capturar_nome = self.caixa_produto.get()
            self.capturar_preco = self.caixa_preco.get()
            self.conecta_banco()

            self.selecionar = self.relatorio.item(self.relatorio.selection()[0], 'values')
            self.sql.execute(f'UPDATE produto SET nome_produto =?, preco_produto=? where id=?',
                             (self.capturar_nome, self.capturar_preco, self.selecionar[0]))
            self.conexao.commit()
            self.limpar_dados()

            messagebox.showinfo('Alteração', 'Dados alterados com sucesso!')
            self.mostrar_dados()
            self.desconecta_banco()
        except IndexError:
            messagebox.showerror('Alteração','Selecione um dado para alterar')
            self.desconecta_banco()

    def pesquisar_dados(self):
       self.mostrar_dados()
       try:
         self.pesq = self.caixa_pesquisa.get()
         if self.pesq == '':
            messagebox.showwarning('Erro','Coloque seu nome da pesquisa')
         else:
            self.sql.execute('SELECT * FROM produto WHERE nome_produto LIKE ''' + self.pesq + '%'' ')
            self.dados = self.sql.fetchall()
         if self.dados:
            self.relatorio.delete(*self.relatorio.get_children())
         else:
            messagebox.showwarning('Erro', 'Esse produto não está cadastrado')
         for item in self.dados:
            self.relatorio.insert('', 'end', values=(item))
       except:
           messagebox.showerror('Erro', 'Erro no Banco de Dados! Tente novamente!')

    def multiplo_clique(self, event):
        self.caixa_recebe_id = customtkinter.CTkEntry(self.janela)

        self.relatorio.selection()
        for elemento in self.relatorio.selection():
            coluna1, coluna2, coluna3 = self.relatorio.item(elemento,'values')
            self.caixa_recebe_id.insert(END, coluna1)
            self.caixa_produto.insert(END, coluna2)
            self.caixa_preco.insert(END, coluna3)


#----------------------- Chamando a classe ModeloSistema -----------------
windows = customtkinter.CTk()
objeto = ModeloTelaPrincipal(windows)
windows.mainloop()'''
