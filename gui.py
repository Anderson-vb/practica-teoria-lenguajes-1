from tkinter import *
from tkinter import font
from estado import Estado
from afd import AFD

def generar_afd():
    valor = regex_input.get()
    estado_inicial = Estado(valor)
    afd = AFD()
    afd.crear_afd(estado_inicial)
    resultado.config(text = afd.mostrar_afd())

# Ventana principal
ventana = Tk()
ventana.title('Practica')
ventana.geometry('550x700')
ventana.config(bg='#001219')

# Label del titulo
titulo = Label(ventana, text='AFD en base a Expresión Regular')
titulo.config(font=('Monospace', 18, font.BOLD), fg='white', bg='#001219')
titulo.grid(row=0, column=0, padx=20, pady=40, columnspan=2)

# Label de el input
mensaje = Label(ventana, text='Ingrese la expresión regular')
mensaje.config(font='Monospace', fg='white', bg='#001219')
mensaje.grid(row=1, column=0, padx=20, pady=20, columnspan=2)

# Input
regex_input = Entry(ventana)
regex_input.config(font='Monospace', bg='#001219', fg='white')
regex_input.grid(row=2, column=0, padx=20, pady=20)

# Boton
button = Button(text='Generar AFD', width=25, command=generar_afd)
button.config(bg='springgreen', borderwidth=0, font='Monospace', highlightbackground='#001219', activebackground='black', activeforeground='white')
button.grid(row=2, column=1, padx=20, pady=20)

# Label donde se mostrará el resultado
resultado = Label(ventana, text = '', justify=LEFT)
resultado.config(font='Monospace', fg='white', bg='#001219')
resultado.grid(row=3, column=0, padx=20, pady=20, columnspan=2)

ventana.mainloop()