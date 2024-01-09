import customtkinter
from banco01 import Backend
from tkinter import messagebox

class ModeloSistema(Backend):
    def __init__(self, windows):
        self.janela = windows
        self.janela.title('Cadastro')
        self.janela.geometry('414x600+450+0')
        self.janela.iconbitmap('imagem/icone.ico')
        self.janela._set_appearance_mode('lithg')
        self.criar_tabela()

        self.titulo = customtkinter.CTkLabel(self.janela, text='Criamos uma nova conta',font=('Poppins Bold',35, 'bold'),
                                             wraplength=250,text_color='black')
        self.titulo.pack()

        self.nome = customtkinter.CTkLabel(self.janela, text='Nome', font=('Courior', 20, 'bold'))
        self.nome.place(x=10,y=150)

        self.caixa_nome = customtkinter.CTkEntry(self.janela, placeholder_text='Seu nome', width=300, height=30,fg_color='#d9d9d9')
        self.caixa_nome.place(x=100,y=150)

        self.senha = customtkinter.CTkLabel(self.janela, text='Senha',font=('Courior',20,'bold'))
        self.senha.place(x=10,y=250)

        self.caixa_senha = customtkinter.CTkEntry(self.janela, placeholder_text='Senha',width=300,height=30,fg_color='#d9d9d9')
        self.caixa_senha.place(x=100,y=250)

        self.confirmacao = customtkinter.CTkLabel(self.janela, text= 'Confirmar senha', font=('Courior', 20, 'bold'))
        self.confirmacao.place(x=10,y=350)

        self.caixa_confirmacao = customtkinter.CTkEntry(self.janela, placeholder_text='Senha', width=200, height=30,fg_color='#d9d9d9')
        self.caixa_confirmacao.place(x=200, y=350)

        self.botao = customtkinter.CTkButton(self.janela, text='Cadastrar', command=self.cadastrar_usuario)
        self.botao.place(x=120,y=450)

        self.botao1 = customtkinter.CTkButton(self.janela, text='Entrar', command=self.entrar)
        self.botao1.place(x=120,y=500)

    def entrar(self):
        self.recebe_nome = self.caixa_nome.get()
        self.recebe_senha = self.caixa_senha.get()
        self.conecta_banco()
        self.sql.execute('''SELECT * FROM usuarios WHERE (username = ? and senha = ? )'''
                          ,(self.recebe_nome, self.recebe_senha))
        self.pesquisa_dados = self.sql.fetchone()
        print(self.pesquisa_dados)
        try:
            if self.recebe_nome in self.pesquisa_dados:
             messagebox.showinfo('Entrar', f'Bem vindo ao programa {self.recebe_nome}')
             self.desconecta_banco()
             self.janela.withdraw()
             self.janela2 = customtkinter.CTkToplevel()
             self.janela2.mainloop()

        except:
            messagebox.showerror('Erro', 'Cadastro não encontrado!')
            self.desconecta_banco()
    def cadastrar_usuario(self):
        self.capturar_nome = self.caixa_nome.get()
        self.capturar_senha = self.caixa_senha.get()
        self.capturar_confirmacao = self.caixa_confirmacao.get()

        self.conecta_banco()
        self.sql.execute('''
            INSERT INTO usuarios (username, senha,confirmaSenha)
            values (?,?,?)
            ''', (self.capturar_nome, self.capturar_senha, self.capturar_confirmacao))
        try:
           if self.capturar_nome == '' or self.capturar_senha == '' or self.capturar_confirmacao == '':
              messagebox.showerror('Sistema de cadastro','Preencha todos os campos!')
           elif len(self.capturar_nome) < 4:
               messagebox.showwarning('Sistema de login','O nome não pode ser menor que 4 caracteres')
           elif len(self.capturar_senha) < 4:
               messagebox.showwarning('Sistema de login','A senha não pode ser menor que 4 caracteres')
           elif self.capturar_senha != self.capturar_confirmacao:
               messagebox.showwarning('Erro!', 'Senhas não coincidem')
           else:
               self.conexao.commit()
               messagebox.showinfo('Cadastro', f'Parabéns! {self.capturar_nome}, Dados Salvos!')
               self.desconecta_banco()
        except:
            messagebox.showerror('Cadastro', 'Erro no processamento do seu cadastro. Tente novamente!')
            self.desconecta_banco()
        self.desconecta_banco()


windows = customtkinter.CTk()
objeto = ModeloSistema(windows)
windows.mainloop()