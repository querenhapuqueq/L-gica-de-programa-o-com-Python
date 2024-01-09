from tkinter import*
import customtkinter
import tkinter

#configuração de tela
class telaInicial():
    def _init_(self, windows):
        self.janela = windows
        self.janela.title('SULLY BANK')
        self.janela.geometry('420x650+450+0')
        self.janela.iconbitmap("imagem/imagem1.png")
        self.janela._set_appearance_mode('black')

        self.imagem = PhotoImage(file='imagem/imagem2.png')
        self.label_imagem = Label(self.janela, image=self.imagem)
        self.label_imagem.place(x=150,y=200)

            #--------------------- Título ---------
        self.titulo = customtkinter.CTkLabel(self.janela,
                                             text=' Bem vindo ao Sully Bank',
                                             font=('Poppins Bold', 35, 'bold'),
                                             text_color='white')
        self.titulo.place(x=750,y=200)

        # --------------------- Label ---------

        self.cpf = customtkinter.CTkLabel(self.janela, text='CPF', font=('Courior', 20, 'bold'))
        self.cpf.place(x=730,y=350)

        self.caixa_cpf = customtkinter.CTkEntry(self.janela, placeholder_text='Digite seu CPF', width=300, height=30,fg_color='black')
        self.caixa_cpf.place(x=800,y=350)

        self.senha = customtkinter.CTkLabel(self.janela, text='Senha', font=('Courior', 20, 'bold'))
        self.senha.place(x=730, y=400)

        self.caixa_senha = customtkinter.CTkEntry(self.janela, placeholder_text='Senha', width=300, height=30,
                                                  fg_color='black')
        self.caixa_senha.place(x=800, y=400)

        # --------------------- Botão ---------

        self.botao = customtkinter.CTkButton(self.janela, text='Entrar')
        self.botao.place(x=920, y=510)

        self.botao1 = customtkinter.CTkButton(self.janela, text='Cadastrar')
        self.botao1.place(x=920, y=550)



windows = customtkinter.CTk()
objeto = telaInicial(windows)
windows.mainloop()