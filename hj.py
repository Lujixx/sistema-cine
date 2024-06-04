import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as smg
from PIL import Image, ImageTk
import os
import cv2

# Variables globales
num_filas = 5
num_columnas = 6
butacas = [[0] * num_columnas for _ in range(num_filas)]
butacas_seleccionadas = []

def mostrar_pelicula(pelicula):
    ventana_detalle = tk.Toplevel(ventana)
    ventana_detalle.title("Detalles de la Película")
    ventana_detalle.geometry("2000x4000")
    ventana_detalle.configure(bg="black")

    estilo = ttk.Style()
    estilo.configure("TLabel", background="black", foreground="white", font=("Helvetica", 12, "bold"))
    ventana_detalle.option_add("*TLabel*highlightBackground", "gold")

    info_pelicula = {
        "Película 1": {
            "sinopsis": "El Justiciero\nHorario: 14:00 - 16:00\nSala: 1",
            "video_path": "INTEGRADOR/archivo/eljusticiero_.mp4"
        },
        "Película 2": {
            "sinopsis": "Rápido y Furioso X\nHorario: 16:30 - 18:30\nSala: 2",
            "video_path": "INTEGRADOR/archivo/rapidosyfuriososX.mp4"
        },
        "Película 3": {
            "sinopsis": "La Monja 2\nHorario: 19:00 - 21:00\nSala: 3",
            "video_path": "INTEGRADOR/archivo/lamonja2_.mp4"
        },
        "Película 4": {
            "sinopsis": "Barbie\nHorario: 22:00 - 00:00\nSala: 4",
            "video_path": "INTEGRADOR/archivo/barbie_.mp4"
        }
    }

    detalles = info_pelicula.get(pelicula, {
        "sinopsis": "Información no disponible"
    })

    titulo_label = ttk.Label(ventana_detalle, text=pelicula, style="TLabel")
    titulo_label.pack(pady=10)
    titulo_label.place(x=50, y=100)

    detalles_label = ttk.Label(ventana_detalle, text=detalles["sinopsis"], style="TLabel")
    detalles_label.pack(pady=10)
    detalles_label.place(x=20, y=100)

    boton_seleccionar_butacas = tk.Button(ventana_detalle, text="Seleccionar Butacas", command=lambda: seleccionar_butacas(pelicula))
    boton_seleccionar_butacas.pack(pady=10)
    boton_seleccionar_butacas.place(x=50, y=200)

    video_path = detalles["video_path"]
    if os.path.exists(video_path):
        cap = cv2.VideoCapture(video_path)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            photo = ImageTk.PhotoImage(Image.fromarray(frame))

            video_label = tk.Label(ventana_detalle, image=photo)
            video_label.image = photo
            video_label.pack()

            ventana_detalle.update()

        cap.release()
    else:
        print("El video no se encontró en la ruta especificada")


def seleccionar_butacas(pelicula):
    global butacas_seleccionadas
    ventana_butacas = tk.Toplevel(ventana)
    ventana_butacas.title(
    ventana_butacas = tk.Toplevel(ventana)
    ventana
"Selección de Butacas")
    ventana_butacas.geometry("400x400")

    pelicula_label = ttk.Label(ventana_butacas, text=f"Película: {pelicula}", font=("Helvetica", 12, "bold"))
    pelicula_label.pack()

    marco_butacas = ttk.Frame(ventana_butacas)
    marco_butacas.pack(padx=
    pelicula_label.pack()

    marco_butacas =

    pelicula_label.pack()

    marco_butacas

    pelicula_label.pack()

    marco_but

    pelic
10, pady=10)

    for fila in range(num_filas):
        for columna in range(num_columnas):
            estado_boton = "normal" if butacas[fila][columna] == 0 else "disabled"
            boton = tk.Button(marco_butacas, text=f"Fila {fila + 1}, Columna {columna + 1}", width=10,
                             state=estado_boton, command=lambda f=fila, c=columna: seleccionar_butaca(f, c))
            boton.grid(row=fila, column=columna)

    reservar_boton = tk.Button(ventana_butacas, text=
            boton.grid(row=fila, column=
"Reservar Butacas", command=lambda: reservar_butacas(pelicula))
    reservar_boton.pack()

def seleccionar_butaca(fila, columna):
    
   
if butacas[fila][columna] == 0:
        butacas[fila][columna] = 1
        butacas_seleccionadas.append((fila, columna))

def reservar_butacas(pelicula):
    global butacas_seleccionadas
    if butacas_seleccionadas:
        mensaje = 
        mensaje
f"¡Ha reservado {len(butacas_seleccionadas)} butacas para la película '{pelicula}' con éxito!"
        seleccion_exitosa = smg.showinfo("Reserva Exitosa", mensaje)
    else:
        mensaje = "Por favor, seleccione al menos una butaca."
        smg.showerror("Error", mensaje)
    butacas_seleccionadas = []

ventana = tk.Tk()
ventana.geometry(
    butacas_seleccionadas = []

vent
"2000x4000")
ventana.title("Cartelera de Cine")
ventana.configure(bg="black")

fuente_personalizada = ("Helvetica", 18, "bold")


imagen1 = Image.open("INTEGRADOR/cartelera_imagen4.png")
imagen1 = imagen1.resize((250, 300))
imagen1 = ImageTk.PhotoImage(imagen1)

imagen2 = Image.open("INTEGRADOR/cartelera_imagen1.png")
imagen2 = imagen2.resize((250, 300))
imagen2 = ImageTk.PhotoImage(imagen2)

imagen3 = Image.open("INTEGRADOR/cartelera_imagen3.png")
imagen3 = imagen3.resize((250, 300))
imagen3 = ImageTk.PhotoImage(imagen3)

imagen4 = Image.open("INTEGRADOR/cartelera_imagen2.png")
imagen4 = imagen4.resize((250, 300))
imagen4 = ImageTk.PhotoImage(imagen4)

etiqueta1 = tk.Label(ventana, font=fuente_personalizada, image=imagen1, compound="top")
etiqueta1.place(x=20, y=50)

etiqueta2 = tk.Label(ventana, font=fuente_personalizada, image=imagen2, compound="top")
etiqueta2.place(x=1025, y=50)

etiqueta3 = tk.Label(ventana, font=fuente_personalizada, image=imagen3, compound="top")
etiqueta3.place(x=20, y=550)

etiqueta4 = tk.Label(ventana, font=fuente_personalizada, image=imagen4, compound="top")
etiqueta4.place(x=1025, y=550)

texto1 = tk.Label(ventana, text="Película 1: El Justiciero", font=fuente_personalizada, fg="white", bg="black")
texto1.place(x=20, y=370)

texto2 = tk.Label(ventana, text="Película 2: Rápido y Furioso X", font=fuente_personalizada, fg="white", bg="black")
texto2.place(x=970, y=370)

texto3 = tk.Label(ventana, text="Película 3: La Monja 2", font=fuente_personalizada, fg="white", bg="black")
texto3.place(x=20, y=875)

texto4 = tk.Label(ventana, text="Película 4: Barbie", font=fuente_personalizada, fg="white", bg="black")
texto4.place(x=1050, y=875)

boton1 = tk.Button(ventana, text="Ver Trailer", command=lambda: mostrar_pelicula("Película 1"), font=fuente_personalizada)
boton1.place(x=70, y=420)

boton2 = tk.Button(ventana, text="Ver Trailer", command=lambda: mostrar_pelicula("Película 2"), font=fuente_personalizada)
boton2.place(x=1070, y=420)

boton3 = tk.Button(ventana, text="Ver Trailer", command=lambda: mostrar_pelicula("Película 3"), font=fuente_personalizada)
boton3.place(x=70, y=925)

boton4 = tk.Button(ventana, text="Ver Trailer", command=lambda: mostrar_pelicula("Película 4"), font=fuente_personalizada)
boton4.place(x=1070, y=925)

sinopsis1 = tk.Text(
    ventana,
    wrap=tk.WORD,
    width=50,
    height=9,
    font=("verdana", 16),
    fg="white",
    bg="black"
)
sinopsis1.insert("1.0", "SINOPSIS: El exagente McCall vive ahora retirado en el sur de Italia. No tarda en descubrir que la mafia está extorsionando a sus nuevos amigos, por lo que regresa a la acción para protegerlos.\nFecha de estreno: 21 de septiembre de 2023 (Argentina)\nDirector: Antoine Fuqua\nAño: 2023\nBasada en: The Equalizer\nGuion: Richard Wenk")
sinopsis1.config(state=tk.DISABLED)
sinopsis1.place(x=300, y=50)

sinopsis2 = tk.Text(
    ventana,
    wrap=tk.WORD,
    width=50,
    height=7,
    font=("verdana", 16),
    fg="white",
    bg="black"
)
sinopsis2.insert("1.0", "SINOPSIS: Francia, 1956. El asesinato de un sacerdote provoca que un mal demoníaco se extienda sin control. La hermana Irene deberá enfrentarse, de nuevo, a la monja satánica Valak.\nFecha de estreno: 7 de septiembre de 2023 (Argentina)\nDirector: Michael Chaves\nAño: 2023")
sinopsis2.config(state=tk.DISABLED)
sinopsis2.place(x=300, y=550)

sinopsis3 = tk.Text(
    ventana,
    wrap=tk.WORD,
    width=45,
    height=8,
    font=("verdana", 16),
    fg="white",
    bg="black"
)
sinopsis3.insert("1.0", "SINOPSIS: Dom Toretto y sus familias se enfrentan al peor enemigo imaginable, uno llegado desde el pasado con sed de venganza, dispuesto a cualquier cosa con tal de destruir todo aquello que Dom ama.\nFecha de estreno: 18 de mayo de 2023 (Argentina)\nDirector: Louis Leterrier\nProductoras: Universal Studios, Original Film, MÁS\nAño: 2023")
sinopsis3.config(state=tk.DISABLED)
sinopsis3.place(x=1300, y=50)

sinopsis4 = tk.Text(
    ventana,
    wrap=tk.WORD,
    width=45,
    height=6,
    font=("verdana", 16),
    fg="white",
    bg="black"
)
sinopsis4.insert("1.0", "SINOPSIS: Después de ser expulsada de Barbieland por no ser una muñeca de aspecto perfecto, Barbie parte hacia el mundo humano para encontrar la verdadera felicidad..\nFecha de estreno: 30 de julio de 2023\nDirector: Michael Brown")
sinopsis4.config(state=tk.DISABLED)
sinopsis4.place(x=1300, y=550)

ventana.mainloop()
