import tkinter as tk
from tkinter import simpledialog, messagebox


# despliega ventana y retorna un texto
def obtener_texto(titulo, mensaje):
    texto_ingresado = simpledialog.askstring(titulo, mensaje)
    if texto_ingresado is not None:
        texto = texto_ingresado
        return texto
    else:
        messagebox.showinfo("Cancelado", "Operación cancelada")
        exit()


# despliega una ventana con un texto
def ventana_texto(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)
    exit()
