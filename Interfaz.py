from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

raiz=Tk()
menubar = Menu(raiz)
filemenu = Menu(menubar)                                                 #Acciones principales
herramientasmenu = Menu(menubar)                                         #Acciones de Herramientas
herramientasreporte = Menu(menubar)                                      #Acciones de Reportes



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
caja1.config(fg= "white",
             bg= "grey")

caja2=Text(raiz,width=65,height=15)
caja2.place(x=590, y=100)
caja2.config(fg= "white",
             bg= "grey")

#conteo de errores
linea = Label(raiz, text="Linea")
linea.place(x=20,y=70)
caja3=Text(raiz,width=4,height=15)
caja3.place(x=20, y=100)
caja3.config(fg= "white",
             bg= "grey")
yscroll.config(command=(caja1.yview, caja2.yview))

#Metodos para la interfaz
def Abrir(): #abrir archivo
    global cadena
    global teeexto
    global nombreArchivo
    global ficheroactual
    caja2.delete(1.0,END)
    caja1.delete(1.0,END)
    file = filedialog.askopenfilename(filetypes =[('Archivo TXT', '*.txt'),('Archivo XML', '*.xml'),('Archivo JS', '*.js'),('Archivo RMT', '*.rmt')])
    if file != "":
        fichero = open(file)
        ficheroactual=file
        nombreArchivo = file.split("/")[-1]
        muchoTexto = fichero.read()
        cadena=muchoTexto
        teeexto=muchoTexto
        caja1.delete(1.0,END)
        caja1.insert("insert",muchoTexto)
        fichero.close()
    else:
        return
    

def nuevoA(): #Nuevo archivo
    if messagebox.askyesno(message="¿Desea continuar?", title="ALERTA") == TRUE:
         Guardarcomo()
         caja1.delete(1.0,END)
         caja2.delete(1.0,END)
         caja3.delete(1.0,END)
    else:
        caja1.delete(1.0,END)
        caja2.delete(1.0,END)
        caja3.delete(1.0,END)
    
def Anal(): #analiza
    global nombreArchivo
    verificarArchivo = nombreArchivo.split(".")[-1]
    if verificarArchivo == "txt":
        print("Analiznado archivo TXT")


        
        analizar1(cadena,nombreArchivo)
        txt=analizar1(cadena,nombreArchivo)
        caja2.insert("insert",txt)
        
        
def guardarU():
    global nombreArchivo
    global ficheroactual
    global teeexto
    if ficheroactual == "":
        print("hola")
    else:
        textt=caja1.get(1.0,END)
        abrirHtml = open(ficheroactual,"w")
        abrirHtml.write(textt)
        abrirHtml.close()

def Guardarcomo():
    global teeexto
    global ficheroactual
    txtTotal=caja1.get(1.0,END)
    guardar = filedialog.asksaveasfile(initialdir= "/", title="Selec file",defaultextension=".txt"
                    , filetypes = (("Archivo txt","*.txt"),("Archivo xml","*.xml"),("all files","*.*")))
    if guardar != None:
        archivo = open(guardar.name,"w")
        archivo.write(txtTotal)
        archivo.close()
        teeexto = guardar
    else:
        return


##Configuracion de la parte visual
raiz.title("JPR EDITOR - 201700355")
#raiz.iconbitmap('D:/Diego/USAC/Vacas_Junio_2021/Compiladores/Lab/Nuevo_PLY/Proyecto_Junio/logo.ico')
raiz.geometry("1150x600")
raiz.config(bg="black")
Titulo = Label(raiz, text="JPR EDITOR")
Titulo.config(fg= "blue",
              bg= "white",
              font=("Verdana",24))
Titulo.place(x=500,y=35)



#----------------------------------MENU DE ARCHIVO-----------------------------------------------
filemenu.add_command(label = "Nuevo", command = nuevoA)
filemenu.add_command(label = "Abrir", command = Abrir)
filemenu.add_command(label = "Guardar", command=guardarU)
filemenu.add_command(label = "Guardar Como", command=Guardarcomo)
menubar.add_cascade(label="Archivo", menu=filemenu)
#----------------------------------MENU DE EDICION---------------------------------------------
menubar.add_command(label = "Edicion", command = raiz.quit)
#----------------------------------MENU DE HERRAMIENTAS----------------------------------------
herramientasmenu.add_command(label = "Interpretar", command = raiz.quit)
herramientasmenu.add_command(label = "Debugger", command = raiz.quit)
menubar.add_cascade(label="Herramientas", menu=herramientasmenu)
#-----------------------------------ANALIZAR--------------------------------------------------
menubar.add_command(label = "Analizar", command=Anal)
#-------------------------------------REPORTES-------------------------------------------------
herramientasreporte.add_command(label = "Reportes Lexicos", command = raiz.quit)
herramientasreporte.add_command(label = "Reportes ARBOL AST", command=raiz.quit)
herramientasreporte.add_command(label = "Reportes de Tabla de Simbolos", command=raiz.quit)
menubar.add_cascade(label="Reportes", menu=herramientasreporte)
#-------------------------------------------------AYUDA-------------------------------------------
menubar.add_command(label = "Ayuda", command = raiz.quit)
#--------------------------------------------SALIR-----------------------------------------------
menubar.add_command(label = "Salir", command = raiz.quit)


#bucle de la aplicacion
raiz.mainloop()
