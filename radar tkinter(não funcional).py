import tkinter
import tkinter.messagebox

janela=tkinter.Tk()
janela.geometry('300x300')

rotulovelocidade= tkinter.Label(janela, text='velocidade do carro:')
rotulovelocidade.pack()

campovelocidade = tkinter.Entry(janela)
campovelocidade.pack()

def multa():
  velocidade = campovelocidade.get()
  if velocidade <= 80:
    tkinter.messagebox.showinfo('tudo certo', 'dirija com segurança')
  if velocidade > 80:
    (velocidade - 80) * 7
    tkinter.messagebox.showerror('PARE!', 'você foi multado em R$ {multa:7.2f}')

botao = tkinter.Button(janela, text='conferir', command=multa)
botao.pack()

janela.mainloop()