import tkinter as tk
from tkinter import messagebox


class Vendedor:
    def __init__(self, nombre: str, apellidos: str, edad: int):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad


    def imprimir(self):
        return f"Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}"


    def verificar_edad(self):
        if self.edad < 0 or self.edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if self.edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")


class AppVendedor:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Vendedor")
        self.root.geometry("400x300")


        # Etiquetas 
        tk.Label(root, text="Nombre:").pack(pady=5)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()


        tk.Label(root, text="Apellidos:").pack(pady=5)
        self.entry_apellidos = tk.Entry(root)
        self.entry_apellidos.pack()


        tk.Label(root, text="Edad:").pack(pady=5)
        self.entry_edad = tk.Entry(root)
        self.entry_edad.pack()


        # Botón de registro
        tk.Button(root, text="Registrar Vendedor", command=self.registrar_vendedor).pack(pady=15)


        # Resultado
        self.resultado = tk.Label(root, text="", justify="left", font=("Courier", 10))
        self.resultado.pack(pady=10)


    def registrar_vendedor(self):
        nombre = self.entry_nombre.get().strip()
        apellidos = self.entry_apellidos.get().strip()
        edad_texto = self.entry_edad.get().strip()


        # Validar campos
        if not nombre or not apellidos or not edad_texto:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return


        try:
            edad = int(edad_texto)
            vendedor = Vendedor(nombre, apellidos, edad)
            vendedor.verificar_edad()
            self.resultado.config(text=vendedor.imprimir())
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error inesperado", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = AppVendedor(root)
    root.mainloop()
