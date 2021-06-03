from tkinter import *
from tkinter import filedialog

raiz=Tk()
menubar = Menu(raiz)

cadena = "vacio"
nombreArchivo = ""
ficheroactual=""

teeexto=""

#se asigna al menu completo
raiz.config(menu = menubar)

yscroll = Scrollbar(raiz)
yscroll.pack(side=RIGHT, fill=Y)

#cajas de texto
caja1=Text(raiz,width=65,height=15)
caja1.place(x=60,y=100)

caja2=Text(raiz,width=65,height=15)
caja2.place(x=590, y=100)

#conteo de errores
linea = Label(raiz, text="Linea")
linea.place(x=20,y=70)
caja3=Text(raiz,width=4,height=15)
caja3.place(x=20, y=100)
yscroll.config(command=(caja1.yview, caja2.yview))

#Metodos para la interfaz
def Abrir(): #abrir archivo
    caja2.delete(1.0,END)
    caja1.delete(1.0,END)
    global ficheroactual
    file = filedialog.askopenfilename(filetypes =[('Archivo HTML', '*.html'),('Archivo CSS', '*.css'),('Archivo JS', '*.js'),('Archivo RMT', '*.rmt')])
    fichero = open(file)
    ficheroactual=file
    global cadena
    global teeexto
    global nombreArchivo
    nombreArchivo = file.split("/")[-1]

    muchoTexto = fichero.read()
    cadena=muchoTexto
    teeexto=muchoTexto
    caja1.delete(1.0,END)
    caja1.insert("insert",muchoTexto)
    fichero.close()

def nuevoA(): #Nuevo archivo
    caja1.delete(1.0,END)
    caja2.delete(1.0,END)
    caja3.delete(1.0,END)

def Anal(): #analiza
    global nombreArchivo
    verificarArchivo = nombreArchivo.split(".")[-1]
    if verificarArchivo == "html":
        print("analizando html")
        analizar1(cadena,nombreArchivo)
        txt=analizar1(cadena,nombreArchivo)
        caja2.insert("insert",txt)
    elif verificarArchivo == "css":
        print("analiznado css")
        analizar2(cadena,nombreArchivo)
        txt = analizar2(cadena,nombreArchivo)
        caja2.insert("insert",txt)
    elif verificarArchivo =="js":
        print("analizando js")
        analizar3(cadena,nombreArchivo)
    elif verificarArchivo =="rmt":
        print("analizando rmt sintactico")
        analizar10(cadena,nombreArchivo)
        txt=analizar10(cadena,nombreArchivo)
        caja2.insert("insert",txt)
        
        
    


def guardarU():
    global nombreArchivo
    global ficheroactual
    global teeexto
    textt=caja1.get(1.0,END)
    abrirHtml = open(ficheroactual,"w")
    abrirHtml.write(textt)
    abrirHtml.close()


    

def Guardarcomo():
    global teeexto
    global ficheroactual
    textt=caja1.get(1.0,END)
    guardar = filedialog.asksaveasfile(title="Guardar Archivo",initialdir="C:",filetypes = (("Archivo de HTML","*.html*"),("Archivo de CSS","*.css*"),("Archivo de JS","*.js*")))
    yguardar = open(guardar,"w+",encoding="UTF-8")
    yguardar.write(textt)
    yguardar.close()
    teeexto = guardar



    


##Configuracion de la parte visual
raiz.title("JPR EDITOR - 201700355")
raiz.iconbitmap('D:/Diego/USAC/Vacas_Junio_2021/Compiladores/Lab/Nuevo_PLY/Proyecto_Junio/logo.ico')
raiz.geometry("1150x600")
raiz.config(bg="black")
Titulo = Label(raiz, text="JPR EDITOR")
Titulo.config(fg= "blue",
              bg= "white",
              font=("Verdana",24))
Titulo.place(x=500,y=35)



#Menu de acciones
menubar.add_command(label = "Nuevo", command = nuevoA)
menubar.add_command(label = "Abrir", command = Abrir)
menubar.add_command(label = "Guardar", command=guardarU)
menubar.add_command(label = "Guardar Como", command=Guardarcomo)
menubar.add_command(label = "Ejecutar Analisis", command=Anal)
menubar.add_command(label = "Salir", command = raiz.quit)

#bucle de la aplicacion
raiz.mainloop()
