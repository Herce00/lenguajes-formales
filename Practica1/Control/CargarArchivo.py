from tkinter import filedialog, messagebox
from io import open
import csv
import sys
sys.path.insert(1,'c:\\Users\\CH\\Documents\\Python\\Lenguajes Formales\\Practica1')
class CargarArchivo():
    def cargarArchivo(self):
        rutaArchivo = filedialog.askopenfilename(title="Ingresar Archivo")
        try:
            with open (rutaArchivo) as data:
                entrada = csv.reader(data, delimiter=",")
                #lista para filtrar herrores al leer el archivo
                filtro = list(entrada)
                condicionFiltro=True
        except:
            messagebox.showerror("Error en la lectura del archivo","Ocurrio un error a la ora de cargar el archivo")
        
        for i in range(len(filtro)):
            if(filtro[i][0]!=""):
                filtro[i][0]=(int)(filtro[i][0])
            else:
                condicionFiltro=False
            for j in range(3,7):
                if(filtro[i][j]!=""):
                    filtro[i][j]=(int)(filtro[i][j])
            if(len(filtro[i])!=7):
                condicionFiltro=False
            if(filtro[i][3]==1 or filtro[i][3]==0):
                condicionFiltro = True
            else :
                condicionFiltro = False
                break
            if (filtro[i][6]==1 or filtro[i][6]==0 or filtro[i][6]==-1):
                condicionFiltro = True
            else:
                condicionFiltro = False
                break

        if(condicionFiltro==False):
            messagebox.showerror("Error en la lectura del archivo","El archivo tiene problemas en alguna Columna o Fila")
        if(condicionFiltro):
            lista = filtro
            messagebox.showinfo("Confirmacion Archivo","Archivo Cargado Exitosamente")
            with open(r"C:\Users\CH\Documents\Python\Lenguajes Formales\Practica1\datos.csv","w",newline="") as archivo:
                escribir = csv.writer(archivo,delimiter=",")
                escribir.writerows(lista)
                archivo.close()
                self.ordenamientoBurbuja()
    
            
    
    
    def ordenamientoBurbuja(self):
        with open (r"C:\Users\CH\Documents\Python\Lenguajes Formales\Practica1\datos.csv") as data:
            entrada = csv.reader(data, delimiter=",")
            lista = list(entrada)
        for i in range(len(lista)):
            lista[i][0]=(int)(lista[i][0])
        condicionBusqueda=False
        for i in range(len(lista)):
            for j in range(len(lista)-1):
                if(lista[j][0]>lista[j+1][0]) or lista[j][0]== lista[j+1][0]:
                    if(lista[j][0]== lista[j+1][0]):
                        condicionBusqueda = True
                        lista[j]=lista[j+1]
                        lista[j+1]=[0]
                        
                    else:
                        aux = lista[j]
                        lista[j]=lista[j+1]
                        lista[j+1]=aux
        if(condicionBusqueda):
            messagebox.showinfo("Aviso Busqueda","Se encontro un datos repetidos se replazara por el más reciente")
            cantidadDeCeros = (int)(lista.count([0]))
            for i in range(cantidadDeCeros):
                lista.remove([0])
        with open(r"C:\Users\CH\Documents\Python\Lenguajes Formales\Practica1\datos.csv","w",newline="") as archivo:
                escribir = csv.writer(archivo,delimiter=",")
                escribir.writerows(lista)
                archivo.close()
                    
        


