'''from tkinter import*
import tkinter
from tkinter import ttk

janela = tkinter.Tk()
janela.geometry('500x200')
label = tkinter.Label(janela)
label.pack()

i = 0
def funcao_progresso():
    global i
    if i <= 10:
        texto = 'Carregando...' + str(10 * i) + '%'

        label.config(text=texto)
        label.after(600, funcao_progresso)
        barra_progresso['value'] = 10 * 1
        i += 1

barra_progresso = ttk.Progressbar(janela)
barra_progresso.pack(pady=50)

funcao_progresso()


def progressao():
    barra['value'] = barra['value'] + 10
    porcentagem['text'] = str(barra['value']) + '%'
    if barra['value'] < 100:
        barra['value'] = barra['value'] + 10
        porcentagem['text'] = str(barra['value']) + '%'
    else:
        porcentagem['text'] = 'Contagem finalizada'


porcentagem = Label(janela, text='0%')
porcentagem.pack()
barra = ttk.Progressbar(janela, length=300)
barra['value'] = 0
barra.pack()
botao = Button(janela, text='Avançar', command=progressao)
botao.pack()



janela.mainloop()'''