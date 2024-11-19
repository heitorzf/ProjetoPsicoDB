import mysql.connector
import tkinter as tk

def mostrarValor(e1 , e2):
    valor = float(e1.get())
    valor2 = float(e2.get())
    print(valor , valor2)
    soma = valor + valor2
    
    print(soma)

window = tk.Tk()
window.geometry("600x600")
window.resizable(False, False)
label = tk.Label(window , text='Cadastro de Pacientes')
window.title('io')
label.pack()
button = tk.Button(window , text='Clicar' ,width=25, command=lambda : mostrarValor(e1 , e2) ) #destroy é para sair da janela 
button.pack()
nome = tk.Label(window, text='Primeiro nome')
sobrenome = tk.Label(window, text='Sobrenome')
e1 = tk.Entry(window)
e2  = tk.Entry(window) 

e1.pack()
e2.pack()
window.mainloop()
