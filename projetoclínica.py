import customtkinter
from tkinter import messagebox
from bancoclínica import Backend

class TelaPrincipal():
    #tela 1, configuração
    def __init__(self, tela):
        self.janela = tela
        self.janela.geometry('500x400')
        self.janela.title('Clínica de odontológia')
        customtkinter.set_appearance_mode('light')

    #itens da tela 1
        self.titulo = customtkinter.CTkLabel(self.janela, text='Login', font=('Ariel', 30, 'bold'))
        self.titulo.pack(pady=12, padx=10)

        self.caixa_cpf = customtkinter.CTkEntry(self.janela, placeholder_text='Digite aqui', font=('Ariel',10), corner_radius=10)
        self.caixa_cpf.pack(pady=12, padx=10)

        self.caixa_senha = customtkinter.CTkEntry(self.janela, placeholder_text='Senha', show='*', corner_radius=10, font=('Ariel',10))
        self.caixa_senha.pack(pady=12, padx=10)

        self.botao_entrar = customtkinter.CTkButton(self.janela, text='Entrar',command=self.entrar)
        self.botao_entrar.pack(pady=12, padx=10)

        self.botao_cadastro = customtkinter.CTkButton(self.janela, text='Cadastro' , command=self.cadastro)
        self.botao_cadastro.pack(pady=12, padx=10)

    def entrar(self):
        self.recebe_cpf = self.caixa_cpf.get()
        self.recebe_senha = self.caixa_senha.get()
        self.conecta_banco()
        self.sql.execute('''SELECT * FROM usuarios WHERE (username = ? and senha = ? )'''
                         , (self.recebe_cpf, self.recebe_senha))
        self.pesquisa_dados = self.sql.fetchone()
        print(self.pesquisa_dados)
        try:
            if self.recebe_cpf in self.pesquisa_dados:
                messagebox.showinfo('Entrar', f'Bem vindo ao programa {self.recebe_cpf}')
                self.desconecta_banco()
                self.janela.withdraw()
                self.janela2 = customtkinter.CTkToplevel()
                self.janela2.mainloop()

        except:
            messagebox.showerror('Erro', 'Cadastro não encontrado!')
            self.desconecta_banco()

    def cadastro(self):
        # configuração da tela cadastro
        self.janela.withdraw()
        self.janela3 = customtkinter.CTkToplevel()
        self.janela3.geometry('500x400')
        self.janela3.title('Clínica de odontológia')
        self.janela3.resizable(width='false', height='false')
        # componentes do janela3


tela = customtkinter.CTk()
objeto = TelaPrincipal(tela)
tela.mainloop()