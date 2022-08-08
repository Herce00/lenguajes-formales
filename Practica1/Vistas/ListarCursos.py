from tkinter import *
from tkinter import ttk
import sys
import csv
from tkinter import messagebox
sys.path.insert(2,'c:\\Users\\CH\\Documents\\Python\\Lenguajes Formales\\Practica1')
from  Vistas.VistaPrincipal import VistaPrincipal2
class ListarCursos():
    
    vistas = VistaPrincipal2()
    framePrincipal = Frame(vistas.raizPrincipal,width=715,height=408)
    tabla = ttk.Treeview(framePrincipal,height=18,columns=("2","3","4","5","6","7"))
    #Creando Entry
    dato=StringVar()
    espacioCodigo = Entry(framePrincipal,width=80,textvariable=dato)
    
    def agregarFrame(self):
        #agregando frame
        self.framePrincipal.pack()
        self.framePrincipal.config(bd=5)
        self.framePrincipal.config(relief="groove")

        #ingresar label
        codigoCurso = Label(self.framePrincipal,text="Codigo Curso:")
        codigoCurso.grid(row =0,column=0)
        #ingresando Entry
        self.espacioCodigo.grid(row=0,column=1)
        #ingresando el boton
        botonBuscar =  Button(self.framePrincipal,text="Buscar",command=lambda:self.buscar())
        botonBuscar.grid(row=0,column=2)

        #columna 1
        self.tabla.column("#0",width=80,anchor=CENTER)
        self.tabla.heading("#0",text="Codigo")
        #columna 2
        self.tabla.column("2",width=200,anchor=CENTER)
        self.tabla.heading("2",text="Nombre")
        #columna 3
        self.tabla.column("3",width=80,anchor=CENTER)
        self.tabla.heading("3",text="Pre requisitos")
        #columna 4
        self.tabla.column("4",width=80,anchor=CENTER)
        self.tabla.heading("4",text="Opcionalidad")
        #columna 5
        self.tabla.column("5",width=80,anchor=CENTER)
        self.tabla.heading("5",text="Semestre")
        #columna 6
        self.tabla.column("6",width=80,anchor=CENTER)
        self.tabla.heading("6",text="Creditos")
        #columna 7
        self.tabla.column("7",width=80,anchor=CENTER)
        self.tabla.heading("7",text="Estado")

        self.tabla.grid(row=1,column=0,columnspan=3)

    def buscar(self):
        try:
            
            dato = (int)(self.dato.get())
            with open (r"C:\Users\CH\Documents\Python\Lenguajes Formales\Practica1\datos.csv") as data:
                entrada = csv.reader(data, delimiter=",")
                lista = list(entrada)
                data.close()
            for i in range(len(lista)):
                lista[i][0] = (int)(lista[i][0])
                if(lista[i][0]==dato):
                    condicionBusqueda =True
                    self.tabla.delete(*self.tabla.get_children())
                    self.tabla.insert("",END,text=lista[i][0],values=(lista[i][1],lista[i][2],lista[i][3],lista[i][4],lista[i][5],lista[i][6]))
                    break
                else:
                    condicionBusqueda =False
            if(condicionBusqueda==False):
                messagebox.showinfo("Confirmacion Busqueda","Dato no encontrado")
        except:
            messagebox.showerror("Dato Erroneo","El dato ingresado no es valido")
        self.dato.set("")
        
        