import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
import subprocess

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menu Cine Cuenca")
ventana.configure(background="black")

def salir():
    ventana.withdraw()

def abrir_Combos():
    ventana.withdraw()
    subprocess.Popen(["python", "combos.py"])

def abrir_estrenos():
    ventana.withdraw()
    subprocess.Popen(["python", "estrenos.py"])

def abrir_Cartelera():
    ventana.withdraw()
    subprocess.Popen(["python", "pythoncartelera.py"])

# Crear botones para las opciones
fuente_facha = ("Bryant Light", 14)
boton_cartelera = tk.Button(ventana, text="Cartelera", font=fuente_facha, command= abrir_Cartelera)
boton_combos = tk.Button(ventana, text="Combos", font=fuente_facha, command= abrir_Combos)
boton_proximos_estrenos = tk.Button(ventana, text="Próximos Estrenos", font=fuente_facha, command= abrir_estrenos)
estrenos = tk.Button(ventana, text="Salir", font=fuente_facha, command= salir )
estrenos.place(x= 350, y = 5)
# Colocar los botones en la parte superior
boton_cartelera.grid(row=0, column=0, padx=5, pady=5, sticky="n")
boton_combos.grid(row=2, column=0, padx=5, pady=5, sticky="n")
boton_proximos_estrenos.grid(row=3, column=0, padx=5, pady=5, sticky="n")

# Cargar la imagen
imagen = PhotoImage(file="foto.jpg")  # Reemplaza "foto.jpg" con la ruta de tu imagen

# Redimensionar la imagen (ajusta el número para cambiar el tamaño)
imagen = imagen.subsample(3)  # Cambia el 2 al valor deseado

# Mostrar la imagen en un widget Canvas
canvas_imagen = tk.Canvas(ventana, width=400, height=200, background="#E4E4E4")
canvas_imagen.grid(row=4, column=0, padx=5, pady=5)
canvas_imagen.create_image(0, 0, anchor=tk.NW, image=imagen)

ventana.mainloop()
