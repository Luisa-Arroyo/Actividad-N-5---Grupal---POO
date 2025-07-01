import tkinter as tk
from tkinter import messagebox, scrolledtext

class LeerArchivoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lector de Archivos")
        self.root.geometry("500x400")

        # Etiqueta y campo para ingresar el nombre del archivo
        tk.Label(root, text="Nombre del archivo (ej: archivo.txt):").pack(pady=5)
        self.entry_nombre = tk.Entry(root, width=40)
        self.entry_nombre.pack(pady=5)
        self.entry_nombre.insert(0, "Tortuga&Liebre.txt")  # valor por defecto

        # Botón para leer el archivo
        tk.Button(root, text="Leer archivo", command=self.leer_archivo).pack(pady=10)

        # Área de texto para mostrar el contenido del archivo
        self.area_texto = scrolledtext.ScrolledText(root, width=60, height=15)
        self.area_texto.pack(padx=10, pady=10)

    def leer_archivo(self):
        nombre = self.entry_nombre.get().strip()

        try:
            with open(nombre, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                self.area_texto.delete("1.0", tk.END)
                self.area_texto.insert(tk.END, contenido)
        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró el archivo: {nombre}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")


# Punto de entrada
if __name__ == "__main__":
    root = tk.Tk()
    app = LeerArchivoGUI(root)
    root.mainloop()
