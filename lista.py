import tkinter as tk


class Celda:
    def __init__(self, contenido):
        self.contenido = contenido
        self.enlace = None  


class CadenaTareas:
    def __init__(self):
        self.inicio = None

 
    def agregar(self, texto):
        nueva = Celda(texto)

        if self.inicio is None:
            self.inicio = nueva
            return

        cursor = self.inicio
        while cursor.enlace is not None:
            cursor = cursor.enlace

        cursor.enlace = nueva

    def obtener_tareas(self):
        resultado = ""
        cursor = self.inicio

        while cursor is not None:
            resultado += "- " + cursor.contenido + "\n"
            cursor = cursor.enlace

        return resultado

class App:
    def __init__(self, root):
        self.lista = CadenaTareas()

        self.root = root
        self.root.title("Gestor de Tareas (Lista Simple)")

        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=10)

        self.boton = tk.Button(root, text="Agregar tarea", command=self.agregar_tarea)
        self.boton.pack(pady=5)

        self.salida = tk.Text(root, width=50, height=15)
        self.salida.pack(pady=10)

    def agregar_tarea(self):
        texto = self.entrada.get()

        if texto != "":
            self.lista.agregar(texto)
            self.actualizar()
            self.entrada.delete(0, tk.END)

    def actualizar(self):
        self.salida.delete(1.0, tk.END)
        self.salida.insert(tk.END, self.lista.obtener_tareas())


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
