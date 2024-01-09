'''from tkinter import *
import customtkinter
def tela_principal():

    janela = Tk()
    janela.title('Sistema de Login')
    janela.geometry('1200x500+100+50')
    janela.iconbitmap('imagem/icone.ico')
    janela.resizable(width=False, height=False)

    def funcao_entrar():
        if login.get() != 'queren' and senha.get() != '2204':
            mensagem['text']= 'Usuário e senha incorretos!'
            limpar_nome()
            limpar_senha()
        elif login.get() != 'queren':
            mensagem['text']= 'Nome de Usuário inválido!'
            limpar_nome()
        elif senha.get() != '2204':
            mensagem['text']= 'Senha incorreta!'
            limpar_senha()
        else:
            janela.withdraw()
            janela1= Toplevel()
            janela1.title('BEM-VINDO')
            janela1.geometry('1200x500+100+50')
            janela1.iconbitmap('imagens/icone.ico')
            janela1.resizable(width=False, height=False)
            janela1.maionloop()




    imagem = PhotoImage(file='imagem/foto1.png')
    label_imagem = Label(janela, image=imagem)
    label_imagem.pack()

    titulo_principal = customtkinter.CTkLabel(janela, text='Faça login ou se cadastre', fg_color='#7F39FB',
                                              font=('Arial', 25))
    titulo_principal.place(x=150, y=10)
    frame_login = customtkinter.CTkFrame(janela, width=500, height=380)
    frame_login.place(x=650, y=80)

    label_titulo = customtkinter.CTkLabel(frame_login, text='Faça seu login', font=('Arial', 20))
    label_titulo.place(x=200, y=10)

    login = customtkinter.CTkEntry(frame_login, width=300, placeholder_text='Seu nome', corner_radius=25)
    login.place(x=100, y=40)

    label_senha = customtkinter.CTkLabel(frame_login, text='Entre com a Senha', font=('Arial', 20))
    label_senha.place(x=190, y=80)

    senha = customtkinter.CTkEntry(frame_login, width=300, placeholder_text='Sua senha', corner_radius=25, show='*')
    senha.place(x=100, y=120)

    botao = customtkinter.CTkButton(frame_login, text= 'Entrar'.upper(), corner_radius=25, hover_color='black',
                                    command=funcao_entrar)
    botao.place(x=200,y=200)

    foto_externa = PhotoImage(file='imagem/c.png')
    botao1= customtkinter.CTkButton(janela, image=foto_externa, compound= 'left', width=200, height=170, anchour='nw')
    botao1.place(x=200,y=200)

    mensagem = Label(frame_login, text='ENTRAR', font=('Arial',15), bg='white')
    mensagem.place(x=150,y=300)

    janela.mainloop()

tela_principal()'''
