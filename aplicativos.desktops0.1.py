''' teste 0.1
from tkinter import*
import tkinter as qh

qh =Tk()
qh.title('GUI DO GERA')
qh['bg']= 'lightblue'
qh.mainloop()
nome1= tk.Label(qh, text='GUI DO GERA', height= 2, width= 35, cursor= 'dot', relief= 'groove', fg= 'black', bg= 'lightblue',
                font=('Arial', 15,'bold'))
nome1.place(x=60,y=20)'''

'''ATIVIDADE INTERFACE GRÁFICA'''
'''1-QUESTÃO
from tkinter import*
import tkinter as qh

qh = Tk()
qh.title('GUI DO GERA')
qh['bg']= 'black'
qh.geometry('300x200+550+100')
qh.resizable(width=False, height=False)
qh.mainloop()'''

'''2-QUESTÃO
from tkinter import*
import tkinter as qhq

qh = Tk()
qh.title('GUI DO GERA')
qh['bg']= 'lightblue'

label =qhq.Label(qh, text='Bem-vindo ao gui do gera', height= 2, width= 35, cursor= 'dot', relief= 'groove',
                 fg= 'black', bg= 'lightblue', font=('Arial', 12,'bold'))
label.place(x=60,y=20)

botao1= qhq.Button(qh, text= 'Botão 1', font= ('verdana',12,'bold'))
botao1.place(x=90,y=100)

botao2= qhq.Button(qh, text= 'Botão 2', font= ('verdana',12,'bold'))
botao2.place(x=190,y=100)

qh.mainloop()'''

'''3-QUESTÃO'''

'''5-QUESTÃO
from tkinter import*
import tkinter as qhv

qh= Tk()
botao1 = qhv.Button(qh, text='botão 1', font=('Ariel',20))
botao1.place(x=200,y=20)
botao2 = qhv.Button(qh, text='botão 2', font=('Ariel',20))
botao2.place(x=150,y=80)
botao3 = qhv.Button(qh, text='botão 3', font=('Ariel',20))
botao3.place(x=270,y=80)
botao4 = qhv.Button(qh, text='botão 4', font=('Ariel',20))
botao4.place(x=90,y=150)
botao5 = qhv.Button(qh, text='botão 5', font=('Ariel',20))
botao5.place(x=220,y=150)
botao6 = qhv.Button(qh, text='botão 6', font=('Ariel',20))
botao6.place(x=340,y=150)
qh.mainloop()'''