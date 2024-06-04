import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import json
import subprocess  

def retrocederMenu(combos):
    combos.withdraw()
    subprocess.Popen(["python", "menu.py"])


def avisoReserva(combo):
    msg.showinfo("Aviso", message="Su reserva fue registrada con éxito")
    guardar_reserva(combo)

def guardar_reserva(combo):
    info_combos = {
        "Combo 1": "2 Gaseosas x 500cc\n1 Pochoclo Grande\n$2500",
        "Combo 2": "2 Gaseosas x 500cc\n2 Panchos\n$3000",
        "Combo 3": "1 Gaseosa x 500cc\n1 Pochoclo Chico\n$1500",
        "Combo 4": "1 Gaseosa x 500cc\n1 Pancho\n$1800"
    }

    # Verificar si el combo seleccionado está en info_combos
    if combo in info_combos:
        # Obtener los detalles del combo
        detalles = info_combos[combo]

        # Guardar los datos en un archivo JSON
        reserva_data = {
            "Combo": combo,
            "Detalles": detalles,
            "Precio": detalles.split('$')[-1].strip()  # Extraer el precio
        }

        try:
            with open("combosGuardados.json", "a") as json_file:
                json.dump(reserva_data, json_file, indent=4)
        except Exception as e:
            msg.showerror("Error", f"No se pudo guardar la reserva: {str(e)}")

def mostrar_combo(combo):
    ventana_detalle = tk.Toplevel(ventana)
    ventana_detalle.title("Detalles del Combo")
    ventana_detalle.geometry("300x300")

    estilo = ttk.Style()
    estilo.configure("TLabel", background="black", foreground="white", font=("Helvetica", 18, "bold"))
    ventana_detalle.option_add("*TLabel*highlightBackground", "gold")

    info_combos = {
        "Combo 1": "2 Gaseosas x 500cc\n1 Pochoclo Grande\n$2500",
        "Combo 2": "2 Gaseosas x 500cc\n2 Panchos\n$3000",
        "Combo 3": "1 Gaseosa x 500cc\n1 Pochoclo Chico\n$1500",
        "Combo 4": "1 Gaseosa x 500cc\n1 Pancho\n$1800"
    }

    detalles = info_combos.get(combo, "Información no disponible")
    etiqueta_detalles = ttk.Label(ventana_detalle, text=detalles)
    etiqueta_detalles.pack()
    boton11 = tk.Button(ventana_detalle, text="Reservar", command=lambda: avisoReserva(combo))
    boton11.place(x=90, y=150)
    boton11.config(font=("Arial", 20))

ventana = tk.Tk()
ventana.geometry("2000x4000")
ventana.title("Combos")
ventana.configure(bg="black")

fuente_personalizada = ("Helvetica", 18, "bold")

imagen1 = Image.open("C:/Users/Fabricio/Desktop/Modulo registro/1.jpg")
imagen1 = imagen1.resize((200, 250))
imagen1 = ImageTk.PhotoImage(imagen1)

imagen2 = Image.open("C:/Users/Fabricio/Desktop/Modulo registro/2.jpg")
imagen2 = imagen2.resize((200, 250))
imagen2 = ImageTk.PhotoImage(imagen2)

imagen3 = Image.open("C:/Users/Fabricio/Desktop/Modulo registro/3.jpg")
imagen3 = imagen3.resize((200, 250))
imagen3 = ImageTk.PhotoImage(imagen3)

imagen4 = Image.open("C:/Users/Fabricio/Desktop/Modulo registro/4.jpg")
imagen4 = imagen4.resize((200, 250))
imagen4 = ImageTk.PhotoImage(imagen4)

etiqueta1 = tk.Label(ventana, font=fuente_personalizada, image=imagen1, compound="top")
etiqueta1.place(x=400, y=50)
etiqueta1.image = imagen1

etiqueta2 = tk.Label(ventana, font=fuente_personalizada, image=imagen2, compound="top")
etiqueta2.place(x=750, y=50)
etiqueta2.image = imagen2

etiqueta3 = tk.Label(ventana, font=fuente_personalizada, image=imagen3, compound="top")
etiqueta3.place(x=400, y=370)
etiqueta3.image = imagen3

etiqueta4 = tk.Label(ventana, font=fuente_personalizada, image=imagen4, compound="top")
etiqueta4.place(x=750, y=370)
etiqueta4.image = imagen4

boton1 = tk.Button(ventana, text="Ver Detalles", command=lambda: mostrar_combo("Combo 1"), font=fuente_personalizada)
boton1.place(x=425, y=310)

boton2 = tk.Button(ventana, text="Ver Detalles", command=lambda: mostrar_combo("Combo 2"), font=fuente_personalizada)
boton2.place(x=775, y=310)

boton3 = tk.Button(ventana, text="Ver Detalles", command=lambda: mostrar_combo("Combo 3"), font=fuente_personalizada)
boton3.place(x=425, y=630)

boton4 = tk.Button(ventana, text="Ver Detalles", command=lambda: mostrar_combo("Combo 4"), font=fuente_personalizada)
boton4.place(x=775, y=630)

botonRetroceder = tk.Button(ventana, text="Atras", command=lambda: retrocederMenu(ventana), font=fuente_personalizada)
botonRetroceder.place(x=200, y=630)

ventana.mainloop()







