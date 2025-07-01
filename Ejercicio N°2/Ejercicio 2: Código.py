import tkinter as tk
from tkinter import messagebox
import math


class CalculosNumericos:
    @staticmethod
    def logaritmo_neperiano(valor: float) -> float:
        if valor <= 0:
            raise ValueError("El valor debe ser positivo para calcular el logaritmo.")
        return math.log(valor)


    @staticmethod
    def raiz_cuadrada(valor: float) -> float:
        if valor < 0:
            raise ValueError("El valor debe ser positivo para calcular la raíz cuadrada.")
        return math.sqrt(valor)


class AppCalculos:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos Numéricos")
        self.root.geometry("400x250")


        # Etiqueta
        tk.Label(root, text="Ingrese un número:").pack(pady=10)
        self.entry_valor = tk.Entry(root)
        self.entry_valor.pack()


        # Botones
        tk.Button(root, text="Calcular logaritmo neperiano", command=self.calcular_log).pack(pady=5)
        tk.Button(root, text="Calcular raíz cuadrada", command=self.calcular_raiz).pack(pady=5)


        # Resultado
        self.lbl_resultado = tk.Label(root, text="", font=("Courier", 10))
        self.lbl_resultado.pack(pady=10)


    def obtener_valor(self):
        valor_texto = self.entry_valor.get().strip()
        if not valor_texto:
            raise ValueError("Debe ingresar un valor.")
        try:
            return float(valor_texto)
        except ValueError:
            raise ValueError("Ingrese un número válido.")


    def calcular_log(self):
        try:
            valor = self.obtener_valor()
            resultado = CalculosNumericos.logaritmo_neperiano(valor)
            self.lbl_resultado.config(text=f"ln({valor}) = {resultado:.5f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


    def calcular_raiz(self):
        try:
            valor = self.obtener_valor()
            resultado = CalculosNumericos.raiz_cuadrada(valor)
            self.lbl_resultado.config(text=f"√{valor} = {resultado:.5f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = AppCalculos(root)
    root.mainloop()
