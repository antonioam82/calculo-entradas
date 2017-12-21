from tkinter import*
from tkinter import messagebox

        
def suma():
    try:
        Salida=Text(ventana,width=20,height=1)
        Salida.insert(INSERT,"")
        Salida.place(x=10,y=218)
        solucion=numero1.get()+numero2.get()
        print(solucion)
        Salida.insert(INSERT,solucion)
    except:
        messagebox.showwarning("ERROR","Operación no válida")

def resta():
    try:
        Salida=Text(ventana,width=20,height=1)
        Salida.insert(INSERT,"")
        Salida.place(x=10,y=218)
        solucion=numero1.get()-numero2.get()
        print(solucion)
        Salida.insert(INSERT,solucion)
    except:
        messagebox.showwarning("ERROR","Operación no válida")

def multi():
    try:
        Salida=Text(ventana,width=20,height=1)
        Salida.insert(INSERT,"")
        Salida.place(x=10,y=218)
        solucion=numero1.get()*numero2.get()
        print(solucion)
        Salida.insert(INSERT,solucion)
    except:
        messagebox.showwarning("ERROR","Operación no válida")
        
def division():
    try:
        Salida=Text(ventana,width=20,height=1)
        Salida.insert(INSERT,"")
        Salida.place(x=10,y=218)
        solucion=numero1.get()/numero2.get()
        print(solucion)
        Salida.insert(INSERT,solucion)
    except:
        messagebox.showwarning("ERROR","Operación no válida")

ventana=Tk()
numero1=IntVar()
numero2=IntVar()
ventana.geometry("400x400")
ventana.title("Entradas numericas")
etiqueta4=Label(ventana,text="numero1").place(x=10,y=10)
numero1Caja=Entry(ventana,textvariable=numero1).place(x=120,y=10)
etiqueta5=Label(ventana,text="numero2").place(x=10,y=40)
numero2Caja=Entry(ventana,textvariable=numero2).place(x=120,y=40)
boton=Button(ventana,text="Hacer suma",command=suma).place(x=10,y=100)
boton2=Button(ventana,text="Hacer resta",command=resta).place(x=10,y=130)
boton3=Button(ventana,text="Hacer multiplicacion",command=multi).place(x=10,y=160)
boton4=Button(ventana,text="Hacer division",command=division).place(x=10,y=190)
Salida=Text(ventana,width=20,height=1)
Salida.insert(INSERT,"")
Salida.place(x=10,y=218)
ventana.mainloop()

