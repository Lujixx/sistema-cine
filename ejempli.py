import tkinter as tk
from tkinter import ttk

def mostrar_pelicula(pelicula):
    ventana_detalle = tk.Toplevel(ventana)
    ventana_detalle.title("Detalles de la Película")
    ventana_detalle.geometry("400x300")

    # Estilo para la ventana emergente
    estilo = ttk.Style()
    estilo.configure("TLabel", background="black", foreground="white", font=("Helvetica", 12, "bold"))
    ventana_detalle.option_add("*TLabel*highlightBackground", "gold")

    # Información de la película
    info_pelicula = {
        "Película 1": "El Justiciero\nHorario: 14:00 - 16:00\nSala: 1",
        "Película 2": "Rápido y Furioso X\nHorario: 16:30 - 18:30\nSala: 2",
        "Película 3": "La Monja 2\nHorario: 19:00 - 21:00\nSala: 3",
        "Película 4": "Barbie\nHorario: 22:00 - 00:00\nSala: 4"
    }

    detalles = info_pelicula.get(pelicula, "Información no disponible")
    etiqueta_detalles = ttk.Label(ventana_detalle, text=detalles)
    etiqueta_detalles.pack()

# Pantalla principal
ventana = tk.Tk()
ventana.geometry("1000x1000")
ventana.title("Cartelera de Cine")
ventana.configure(bg="black")

# Etiquetas y botones con fuente personalizada
fuente_personalizada = ("Helvetica", 14, "bold")  # Modificar el tamaño de la fuente aquí

etiqueta1 = tk.Label(ventana, text="Película 1: El Justiciero", font=fuente_personalizada)
etiqueta1.place(x=20, y=50)
etiqueta2 = tk.Label(ventana, text="Película 2: Rápido y Furioso X", font=fuente_personalizada)
etiqueta2.place(x=20, y=150)
etiqueta3 = tk.Label(ventana, text="Película 3: La Monja 2", font=fuente_personalizada)
etiqueta3.place(x=20, y=250)
etiqueta4 = tk.Label(ventana, text="Película 4: Barbie", font=fuente_personalizada)
etiqueta4.place(x=20, y=350)

boton1 = tk.Button(ventana, text="Ver Detalles", command=lambda: mostrar_pelicula("Película 1"), font=fuente_personalizada)
boton1.place(x=20, y=90)
boton2 = tk.Button(ventana, text="Ver Detalles", command=lambda: mostrar_pelicula("Película 2"), font=fuente_personalizada)
boton2.place(x=20, y=190)
boton3 = tk.Button(ventana, text="Ver Detalles", command=lambda: mostrar_pelicula("Película 3"), font=fuente_personalizada)
boton3.place(x=20, y=290)
boton4 = tk.Button(ventana, text="Ver Detalles", command=lambda: mostrar_pelicula("Película 4"), font=fuente_personalizada)
boton4.place(x=20, y=390)

ventana.mainloop()
