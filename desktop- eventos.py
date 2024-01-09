'''1-questão
from tkinter import*
from tkinter import messagebox


janela = Tk()
janela.title('Meu primeiro progrma')
janela.geometry('400x400+540+150')

def resposta(event):
    messagebox.showinfo('caixa de mensagem', 'evento clique')

label= Label(janela, text='Abrir caixa', relief='raised')
label.pack(pady=20)
label.bind('<Button-1>', resposta)
label.bind('<Button-2>', resposta)

janela.mainloop()'''

'''2-QUESTÃO
from tkinter import*
from tkinter import messagebox

janela = Tk()
janela.title('Primeira tela')
janela.geometry('400x400+540+150')

def nome(nome):
    nome = Label(janela, text='Escreva seu nome: ', font=('Arial', 12,'bold'))
nome.pack()

nome(nome)

entrada = Entry(janela, font=('Arial',12, 'bold'))
entrada.pack()

botao= Button(janela, text='Executar')
botao.pack()

resultado= Label(janela, text='O teu nome é:', font=('Arial',12,'bold'))
resultado.pack()

janela.mainloop()'''

