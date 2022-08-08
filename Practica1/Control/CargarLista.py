import sys
sys.path.insert(2,'c:\\Users\\CH\\Documents\\Python\\Lenguajes Formales\\Practica1')
from Vistas.ListarCursos import ListarCursos
import csv
from tkinter import *
from tkinter import ttk
class CargarDatos():

    from Vistas.VistaPrincipal import VistaPrincipal2
    vista = ListarCursos()
    vista2 = VistaPrincipal2()
    #archivo = CargarArchivo()
    def cargarDatos(self):
        with open (r"C:\Users\CH\Documents\Python\Lenguajes Formales\Practica1\datos.csv") as data:
            entrada = csv.reader(data, delimiter=",")
            lista = list(entrada)
            

        self.vista2.framePrincipal.destroy()
        self.vista.tabla.delete(*self.vista.tabla.get_children())
        for i in range(len(lista)):
            self.vista.tabla.insert("",END,text=lista[i][0],values=(lista[i][1],lista[i][2],lista[i][3],lista[i][4],lista[i][5],lista[i][6]))
        self.vista.agregarFrame()

