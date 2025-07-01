import tkinter as tk
from tkinter import messagebox


class Programador:
    def __init__(self, nombre: str, apellidos: str):
        self.validar_datos(nombre, apellidos)
        self.nombre = nombre
        self.apellidos = apellidos


    @staticmethod
    def validar_datos(nombre, apellidos):
        for campo, valor in [("Nombre", nombre), ("Apellidos", apellidos)]:
            if not valor.isalpha():
                raise ValueError(f"{campo} debe contener solo letras.")
            if len(valor) >= 20:
                raise ValueError(f"{campo} no puede tener 20 o más caracteres.")



class Equipo:
    def __init__(self, nombre_equipo: str, universidad: str, lenguaje: str, tamano: int):
        if tamano < 2 or tamano > 3:
            raise ValueError("El equipo debe tener entre 2 y 3 integrantes.")
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano = tamano
        self.programadores = []


    def esta_completo(self):
        return len(self.programadores) >= self.tamano


    def agregar_programador(self, programador: Programador):
        if self.esta_completo():
            raise Exception("El equipo ya está completo.")
        self.programadores.append(programador)


    def __str__(self):
        datos = f"Equipo: {self.nombre_equipo}\nUniversidad: {self.universidad}\nLenguaje: {self.lenguaje}\nTamaño: {self.tamano}\n"
        datos += "Integrantes:\n"
        for i, prog in enumerate(self.programadores, start=1):
            datos += f"  {i}. {prog.nombre} {prog.apellidos}\n"
        return datos



class AppEquipo:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Equipo de Programación")
        self.root.geometry("500x500")


        # Entrada
        self.equipo = None


        # Seccion: Datos del equipo
        frame_equipo = tk.LabelFrame(root, text="Datos del Equipo")
        frame_equipo.pack(fill="x", padx=10, pady=10)


        self.entries_equipo = {}
        campos = [("Nombre del equipo", "nombre_equipo"),
                  ("Universidad", "universidad"),
                  ("Lenguaje", "lenguaje"),
                  ("Tamaño (2-3)", "tamano")]


        for i, (etiqueta, key) in enumerate(campos):
            tk.Label(frame_equipo, text=etiqueta).grid(row=i, column=0, sticky="e", pady=3)
            entry = tk.Entry(frame_equipo)
            entry.grid(row=i, column=1, pady=3)
            self.entries_equipo[key] = entry


        tk.Button(frame_equipo, text="Crear equipo", command=self.crear_equipo).grid(row=4, columnspan=2, pady=5)


        # Seccion: Añadir programador
        frame_prog = tk.LabelFrame(root, text="Añadir Programador")
        frame_prog.pack(fill="x", padx=10, pady=10)


        tk.Label(frame_prog, text="Nombre").grid(row=0, column=0, pady=3)
        tk.Label(frame_prog, text="Apellidos").grid(row=1, column=0, pady=3)
        self.entry_nombre = tk.Entry(frame_prog)
        self.entry_apellidos = tk.Entry(frame_prog)
        self.entry_nombre.grid(row=0, column=1)
        self.entry_apellidos.grid(row=1, column=1)


        tk.Button(frame_prog, text="Agregar", command=self.agregar_programador).grid(row=2, columnspan=2, pady=5)


        # Resultado
        self.text_resultado = tk.Text(root, height=10)
        self.text_resultado.pack(padx=10, pady=10, fill="both")


    def crear_equipo(self):
        try:
            nombre = self.entries_equipo["nombre_equipo"].get().strip()
            universidad = self.entries_equipo["universidad"].get().strip()
            lenguaje = self.entries_equipo["lenguaje"].get().strip()
            tamano = int(self.entries_equipo["tamano"].get().strip())


            if not all([nombre, universidad, lenguaje]):
                raise ValueError("Todos los campos deben estar llenos.")


            self.equipo = Equipo(nombre, universidad, lenguaje, tamano)
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, "Equipo creado correctamente.\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def agregar_programador(self):
        if self.equipo is None:
            messagebox.showwarning("Advertencia", "Primero cree un equipo.")
            return


        try:
            nombre = self.entry_nombre.get().strip()
            apellidos = self.entry_apellidos.get().strip()
            prog = Programador(nombre, apellidos)
            self.equipo.agregar_programador(prog)


            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, str(self.equipo))


            if self.equipo.esta_completo():
                messagebox.showinfo("Completado", "¡El equipo ya está completo!")


        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = AppEquipo(root)
    root.mainloop()
