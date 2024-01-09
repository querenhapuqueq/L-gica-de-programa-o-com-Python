import customtkinter
from tkinter import*


janela = Tk()
janela.title('combobox')
janela.geometry('700x200+100+50')

def funcao_escolha_linguagem(escolha_linguagem):
    mensagem['text'] = escolha_linguagem

combobox = customtkinter.CTkComboBox(janela, values=['Python', 'Java', 'Portugol'],command=funcao_escolha_linguagem)
combobox.set('Escolha a linguagem')
combobox.pack(pady = 25)

mensagem = Label(janela, text= 'Você escolheu:')
mensagem.pack()

janela.mainloop()