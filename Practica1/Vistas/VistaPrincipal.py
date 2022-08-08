import sys
sys.path.insert(2,'c:\\Users\\CH\\Documents\\Python\\Lenguajes Formales\\Practica1')
from Control.CargarArchivo import CargarArchivo
from tkinter import *
class VistaPrincipal2():
    
    
    cargar = CargarArchivo()
    raizPrincipal= Tk()
    framePrincipal = Frame(raizPrincipal,width=715,height=408)
    
    def __init__(self):
        pass
    
    def modificarRaiz(self):
        from Control.CargarLista import CargarDatos
        Cursos = CargarDatos()
        #modificando el titulo de la ventana raiz y una barra de menus con sub menus
        self.raizPrincipal.title("Vista Principal")
        menuPrincipal = Menu(self.raizPrincipal)
        self.raizPrincipal.config(menu=menuPrincipal)

        #menu archivo con sus sub menus
        archivoMenu = Menu(menuPrincipal,tearoff=0)
        menuPrincipal.add_cascade(label="Archivo",menu=archivoMenu)
        archivoMenu.add_command(label="Cargar Archivo",command=lambda:self.cargar.cargarArchivo())

        #menu Gestionar cursos con sus sub menus
        archivoMenu = Menu(menuPrincipal,tearoff=0)
        menuPrincipal.add_cascade(label="Gestionar Cursos",menu=archivoMenu)
        #primer sub menu
        archivoMenu.add_command(label="Listar Cursos",command=lambda:Cursos.cargarDatos())
        #segundo sub menu
        archivoMenu.add_command(label="Agregar Curso",command=lambda:CargarArchivo.archivo())
        #tercero sub menu
        archivoMenu.add_command(label="Editar Curso",command=lambda:CargarArchivo.archivo())
        #cuarto sub menu
        archivoMenu.add_command(label="Eliminar Curso",command=lambda:CargarArchivo.archivo())
        
        #menu Creditos con sus sub menus
        archivoMenu = Menu(menuPrincipal,tearoff=0)
        menuPrincipal.add_cascade(label="Créditos",menu=archivoMenu)
        archivoMenu.add_command(label="Conteo de Créditos",command=lambda:CargarArchivo.archivo())


    
    def vistaPrincipal(self):
        self.modificarRaiz()
        self.framePrincipal.pack()
        self.framePrincipal.config(bd=5)
        self.framePrincipal.config(relief="groove")
        imagen = PhotoImage(file = r"C:\Users\CH\Documents\Python\Lenguajes Formales\Practica1\Vistas\principal.png")
        imagen2 = Label(self.framePrincipal,image=imagen)
        imagen2.place(x=0,y=0)
        nombreCurso = Label(self.framePrincipal,text="Curso: Lab. Lenguajes Formales y de Programacion. Seccion: A+",font="times",bg="gray")
        nombreCurso.place(x=10,y=100)
        nombreEstudiante = Label(self.framePrincipal,text="Estudiante: César Rolando Hernández Palacios",font="times",bg="gray")
        nombreEstudiante.place(x=10,y=120)
        carnet = Label(self.framePrincipal,text="Carné: 202000806",font="times",bg="gray")
        carnet.place(x=10,y=140)
        self.raizPrincipal.mainloop()
    def hola(self):
        self.framePrincipal.destroy()