import tkinter as tk
from tkinter import messagebox

class PruebaExcepciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Prueba de Excepciones")
        self.ventana.geometry("400x300")

        self.resultado = tk.Text(self.ventana, height=12, width=45)
        self.resultado.pack(pady=10)

        btn_ejecutar = tk.Button(self.ventana, text="Ejecutar código", command=self.ejecutar)
        btn_ejecutar.pack()

    def ejecutar(self):
        self.resultado.delete("1.0", tk.END)

        # Primer bloque try
        try:
            self.resultado.insert(tk.END, "Ingresando al primer try\n")
            cociente = 10000 / 0  # Genera ArithmeticException
            self.resultado.insert(tk.END, "Después de la división\n")
        except ZeroDivisionError:
            self.resultado.insert(tk.END, "División por cero\n")
        finally:
            self.resultado.insert(tk.END, "Ingresando al primer finally\n\n")

        # Segundo bloque try
        try:
            self.resultado.insert(tk.END, "Ingresando al segundo try\n")
            objeto = None
            objeto.toString()  # Genera AttributeError
            self.resultado.insert(tk.END, "Imprimiendo objeto\n")
        except ZeroDivisionError:
            self.resultado.insert(tk.END, "División por cero\n")
        except Exception:
            self.resultado.insert(tk.END, "Ocurrió una excepción\n")
        finally:
            self.resultado.insert(tk.END, "Ingresando al segundo finalmente\n")

# Código principal
if __name__ == "__main__":
    root = tk.Tk()
    app = PruebaExcepciones(root)
    root.mainloop()
