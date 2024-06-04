from pickletools import long1
import json
import string
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import tkinter as tk
from turtle import color
from tkinter import Tk, Label
from PIL import ImageTk, Image
import ttkbootstrap as btp #se importa bootstrap 
import subprocess

ventanaLogin = btp.Window(themename="darkly") #ventana aplicada con bootstrap

def guardarDatos(entryUsuario, entryPassa):#funcion que guarda los elementos a nuestro archivos json
    try:
        datoUsuario = entryUsuario.get()
        contraseñaUsuario = entryPassa.get()

        # Cargar los datos existentes del archivo JSON (si hay alguno)
        datos = []
        try:
            with open("usuarios.json", "r") as json_file:
                datos = json.load(json_file)
        except FileNotFoundError:
            pass

        for usuario_registrado in datos:
            if usuario_registrado["Usuario"] == datoUsuario:
                msg.showerror("Error", "El usuario ya está registrado")
                return  # Salir de la función si el usuario ya existe

        # Agregar un nuevo usuario a la lista de datos
        nuevo_usuario = {
            "Usuario": datoUsuario,
            "Contrasena": contraseñaUsuario
        }
        datos.append(nuevo_usuario)

        # Guardar los datos en el archivo JSON
        with open("usuarios.json", "w") as json_file: 
            json.dump(datos, json_file, indent=4)

        msg.showinfo("Exito", "Usuario y contraseña registrado")
        ventanaLogin.deiconify()
        

    except Exception as e:
        msg.showerror("Error", "Se produjo un error al registrar al usuario: ")

    
def retroceder(ventanaRegistro): #sirve para poder volver al menu de login desde el menu de registro
  ventanaRegistro.withdraw() #oculta la ventana
  ventanaLogin.deiconify()

checkContraseñaVar = tk.BooleanVar()

def ocultarContraseña(entryPassa): #sirve para ocultar la contraseña que ingresa el usuario mediante un check
    if checkContraseñaVar.get() == True:
        entryPassa.config(show="")
    else:
        entryPassa.config(show="*")


def abrir_Menu(): #sirve para importar los demas modulos de la misma carpeta
    subprocess.Popen(["python", "menu.py"])
    ventanaLogin.withdraw()
    ventanaLogin.withdraw()
    
#---------- parte  del registro, qu enom me tome los campos en vacios------------------

def fnRegistrarse():  # Funcion que crea la interfaz de la ventana registrarse y llama a la funcion que va a validar la misma
    ventanaLogin.withdraw()
    def fnValidarDatosRegistro():
        

        if len(varUsuario.get()) >= 6 and len(varUsuario.get()) <= 12:
            msg.showinfo("Bienvenido", "Usuario Registrado")
        else:
              msg.showerror('Error', message= 'El nombre de usuario debe contener al menos 6 y menos de 12 caracteres')

        contrasaeña = varContraseña.get()
        espacio =   mayuscula = minuscula = False
        alfanumerico =  contrasaeña.isalnum()
        for letra in contrasaeña:
            if letra.isspace()==True:
              espacio=True
            if letra.isupper()== True:
              mayuscula=True
            if letra.islower()== True:
              minuscula=True
            if espacio ==  True:
              msg.showerror("Error", "La contraseña no puede contener espacios")
            elif  len(contrasaeña) < 6:
              msg.showerror("Error", "La contraseña debe tener minimo 6 caracteres")
            elif mayuscula == False:
              msg.showerror("Error", "La contraseña debe tener una mayúscula") 
            elif  minuscula == False:
              msg.showerror("Error", "La contraseña debe tener una minúscula")
            elif alfanumerico == True:
              msg.showerror("Error", "La contraseña debe tener algún caracter que no sea alfanúmerico")
        else:
              msg.showinfo("Exito", "Usuario y contraseña correcta")

    
    varUsuario= tk.StringVar()
    varPass= tk.StringVar()
    varCorreo = tk.StringVar()


    ventanaRegistro = btp.Window(themename="darkly")
    ventanaRegistro.configure(bg='BLACK')
    ventanaRegistro.geometry('1366x768')
    ventanaRegistro.title('Menu de registro')
    
#-----------------------------------------------------------------------------------------------------------

#etiquetas

    labelUsuario = Label(ventanaRegistro, text = 'INGRESE SU USUARIO', fg= "black", bg= "gold3")         
    labelUsuario.place(x=20,y= 330)

    entryUsuario= Entry(ventanaRegistro) 
    entryUsuario.place(x=20,y=360)

    labelPass = Label(ventanaRegistro, text = 'INGRESE UNA CONTRASEÑA')         
    labelPass.place(x=20,y= 400)

    labelLogin = Label(ventanaRegistro, text = '¿Ya tienes una cuenta?', fg= "black", bg= "gold3")         
    labelLogin.place(x=280,y= 330)

    entryPassa= ttk.Entry(ventanaRegistro, width=26, show="") 
    entryPassa.place(x=20,y=430)

    texto2 = "¡Bienvenido a Cine CUENCA!"
    labelLogo2 = tk.Label(ventanaRegistro, text=texto2, font=("Arial", 24), fg="white", bg="black")
    labelLogo2.place(x= 40, y= 200)


#BOTONES

    botonRegistrar = Button(ventanaRegistro,text='REGISTRAR', fg= "white", bg= "gray", command=lambda: guardarDatos(entryUsuario, entryPassa))
    botonRegistrar.place (x=60,y = 460)

    botonInicio = Button(ventanaRegistro ,text='INICIA SESIÓN', fg= "white", bg= "white", command=lambda: retroceder(ventanaRegistro))
    botonInicio.place (x=300,y = 360)

    checkContraseña = tk.Checkbutton(ventanaRegistro, text= "Ocultar",bg= "black", variable= checkContraseñaVar, command=lambda: ocultarContraseña(entryPassa))
    checkContraseña.place(x= 190, y= 430)


#---------------------------------VENTANA LOGIN---------------------------------##


def login(): #funcion que crea, lee y valida los datos de nuestro archivo json que fueron puestos en el registro
    with open('usuarios.json', 'r') as archivo:
        usuarios = json.load(archivo)

    nombre = entryUsuario2.get()
    contraseñaIngresada = entryContraseña2.get()

    for usuario in usuarios:
        if usuario.get("Usuario") == nombre and usuario.get("Contrasena") == contraseñaIngresada:
            msg.showinfo("Éxito", "Usuario y contraseña correcta")
            abrir_Menu()
            return


    msg.showerror("Error", "Usuario y/o contraseña incorrecta")

ventanaLogin.deiconify()
varNombre= StringVar()
varContraseña= StringVar()


#Creación de intefarz
ventanaLogin.configure(bg='#000000')
ventanaLogin.geometry('1366x768')
ventanaLogin.title('Menu de login')
#fondo= tk.PhotoImage (file="usuario.png")
#MostrarIcon = tk.Label(ventanaLogin, image=fondo).place(x=110,y= 200)


estilo = ttk.Style()
estilo.configure("BW.TLabel", foreground="black",
                background="black",font=("Helvetica", 16))
                
#label
labelUsuario2 = Label(ventanaLogin, text = 'INGRESAR USUARIO', fg= "gold3", bg= "#021f37")         

labelUsuario2.place(x=130,y= 10)

labelNoCuenta = Label(ventanaLogin, text = '¿No tienes una cuenta?', fg= "white", bg= "#021f37")         

labelNoCuenta.place(x=100,y= 370)

entryUsuario2= ttk.Entry(ventanaLogin) 
entryUsuario2.place(x=125,y=40)

labelContraseña = Label(ventanaLogin, text = 'INGRESAR CONTRASEÑA', fg= "white", bg= "#021f37")

labelContraseña.place(x=120,y= 80)
entryContraseña2= ttk.Entry(ventanaLogin) 
entryContraseña2.place(x=124,y=110)

texto = "¡Bienvenido a Cine CUENCA!"
labelLogo = tk.Label(ventanaLogin, text=texto, font=("Arial", 16), fg="white", bg="black")
labelLogo.place(x= 60, y= 270)

#Botones
botonLogin = Button(ventanaLogin,text='Ingresar', command= login)
botonLogin.place (x=160,y = 170)

boton = Button(ventanaLogin,text='Registrar', command= fnRegistrarse)
boton.place (x=240,y = 369)

mainloop()