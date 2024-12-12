import tkinter as tk  # Importamos la librería Tkinter para crear la GUI

# Función que se ejecuta cuando se hace clic en un botón numérico
def button_click(number):
    current = entry.get()  # Obtener el contenido actual del campo de texto
    entry.delete(0, tk.END)  # Borrar el contenido actual del campo de texto
    entry.insert(0, str(current) + str(number))  # Insertar el número clicado al final del contenido actual

# Función para limpiar el campo de texto
def button_clear():
    entry.delete(0, tk.END)  # Borrar todo el contenido del campo de texto

# Función para calcular el resultado
def button_equal():
    try:
        result = str(eval(entry.get()))  # Evaluar la expresión matemática en el campo de texto
        entry.delete(0, tk.END)  # Borrar el contenido actual del campo de texto
        entry.insert(0, result)  # Insertar el resultado en el campo de texto
    except Exception as e:
        entry.delete(0, tk.END)  # Borrar el contenido en caso de error
        entry.insert(0, "Error")  # Mostrar mensaje de error

root = tk.Tk()  # Crear la ventana principal de la aplicación
root.title("Calculadora")  # Establecer el título de la ventana

# Crear el campo de texto donde se mostrarán las entradas y resultados
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)  # Colocar el campo de texto en la cuadrícula de la ventana

# Lista de botones con sus respectivas posiciones en la cuadrícula
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('=', 4, 2), ('C', 4, 0)
]

# Crear y colocar cada botón en la cuadrícula
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, command=button_equal).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, command=button_clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t)).grid(row=row, column=col)

root.mainloop()  # Iniciar el bucle principal de la aplicación
