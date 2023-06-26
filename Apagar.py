# Importa las librerías necesarias
import tkinter as tk  # Librería para crear la interfaz gráfica de usuario
from tkinter import messagebox  # Librería para mostrar ventanas de mensaje
import os  # Librería para interactuar con el sistema operativo
import re  # Librería para usar expresiones regulares

# Define la función que apagará la computadora
def shutdown():
    time_str = time_entry.get()  # Obtiene el tiempo ingresado por el usuario
    unit = time_unit.get()  # Obtiene la unidad de tiempo seleccionada por el usuario

    # Verifica si el tiempo ingresado por el usuario es un número entero
    if not bool(re.match("^[0-9]+$", time_str)):
        # Si no es un número entero, muestra un mensaje de error y termina la función
        messagebox.showerror("Error", "Por favor, introduce un número entero.")
        return

    time = int(time_str)  # Convierte el tiempo ingresado a un número entero

    # Si la unidad de tiempo es 'Horas', convierte el tiempo a minutos
    if unit == 'Horas':
        time *= 60

    # Ejecuta el comando para apagar la computadora después del tiempo especificado
    os.system(f'shutdown /s /t {time * 60}')

# Crea una nueva ventana
root = tk.Tk()
root.geometry('300x200')  # Define el tamaño inicial de la ventana
root.title("Apagar equipo")  # Asigna un título a la ventana

# Crea y empaqueta un etiqueta para el campo de entrada de tiempo
time_entry_label = tk.Label(root, text="Tiempo antes de apagarse:")
time_entry_label.pack()

# Crea y empaqueta un campo de entrada de texto para el tiempo
time_entry = tk.Entry(root)
time_entry.pack()

# Crea una variable de control para el menú de unidades de tiempo
time_unit = tk.StringVar(root)
time_unit.set('Minutos')  # Asigna 'Minutos' como el valor por defecto

# Crea y empaqueta un menú desplegable para las unidades de tiempo
time_unit_menu = tk.OptionMenu(root, time_unit, 'Minutos', 'Horas')
time_unit_menu.pack()

# Crea y empaqueta un botón para iniciar la secuencia de apagado
shutdown_button = tk.Button(root, text="Apagar", command=shutdown)
shutdown_button.pack()

# Comienza el bucle principal de la interfaz gráfica
root.mainloop()
