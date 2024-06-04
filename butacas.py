import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as smg

# Definir la matriz de butacas (por ejemplo, 3 filas y 3 columnas)
num_filas = 10
num_columnas = 10
butacas = [[0] * num_columnas for _ in range(num_filas)]

def mostrar_seleccion_butacas(pelicula):
    def seleccionar_butaca(fila, columna):
        # Función para seleccionar/deseleccionar butacas
        if butacas[fila][columna] == 0:
            butacas[fila][columna] = 1
            botones[fila][columna].config(bg="green")
        else:
            smg.showinfo("Advertencia", "Este asiento ya ha sido seleccionado.")
            
    def confirmar_seleccion(pelicula):
        # Función para confirmar la selección (puedes definir aquí la lógica)
        # Por ejemplo, mostrar un mensaje con las butacas seleccionadas
        butacas_seleccionadas = [f"asiento {fila * num_columnas + columna + 1}" for fila in range(num_filas) for columna in range(num_columnas) if butacas[fila][columna] == 1]
        if butacas_seleccionadas:
            mensaje = f"Ha seleccionado el {', '.join(butacas_seleccionadas)}"
            smg.showinfo("Éxito", "Butacas guardadas, muchas gracias, lo esperamos!")
        else:
            mensaje = "No ha seleccionado ninguna butaca."
        ttk.Label(ventana_butacas, text=mensaje, background="black", foreground="white").pack()

    ventana_butacas = tk.Tk()
    ventana_butacas.title("Selección de Butacas")
    ventana_butacas.geometry("1000x1000")
    ventana_butacas.configure(bg="black")  # Establecer el fondo de la ventana en negro

    # Etiqueta para mostrar la película seleccionada (puedes omitirla si no la necesitas)
    pelicula_label = ttk.Label(ventana_butacas, background="black", foreground="white", text=f"Película: {pelicula}", font=("Helvetica", 12, "bold"))
    pelicula_label.pack()

    # Crear un marco para las butacas
    marco_butacas = ttk.Frame(ventana_butacas)
    marco_butacas.pack(padx=10, pady=10)

    botones = [[None] * num_columnas for _ in range(num_filas)]

    for fila in range(num_filas):
        for columna in range(num_columnas):
            # Utilizar botones para representar las butacas
            num_asiento = fila * num_columnas + columna + 1  # Calcular el número de asiento
            boton = tk.Button(marco_butacas, text=f"Asiento {num_asiento}", width=10,
                             command=lambda f=fila, c=columna: seleccionar_butaca(f, c))
            boton.grid(row=fila, column=columna)
            botones[fila][columna] = boton

    # Botón para confirmar la selección (puedes cambiar su función)
    confirmar_boton = tk.Button(ventana_butacas, text="Confirmar Selección", command=lambda: confirmar_seleccion(pelicula))
    confirmar_boton.pack()

    ventana_butacas.mainloop()

# Abrir la ventana de selección de butacas (puedes cambiar "Película 1" al nombre de la película que desees)
mostrar_seleccion_butacas("Película 1")
