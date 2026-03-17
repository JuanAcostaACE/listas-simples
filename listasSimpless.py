import tkinter as tk


class Celda:
    def __init__(self, contenido):
        self.contenido = contenido
        self.enlace = None
        self.completada = False


class CadenaTareas:
    def __init__(self):
        self.inicio = None

    def agregar(self, texto):
        nueva = Celda(texto)

        if self.inicio is None:
            self.inicio = nueva
        else:
            self._agregar_recursivo(self.inicio, nueva)

    def _agregar_recursivo(self, actual, nueva):
        if actual.enlace is None:
            actual.enlace = nueva
        else:
            self._agregar_recursivo(actual.enlace, nueva)

    def completar(self, indice):
        self._completar_recursivo(self.inicio, indice, 0)

    def _completar_recursivo(self, nodo, objetivo, actual_indice):
        if nodo is None:
            return

        if actual_indice == objetivo:
            nodo.completada = True
            return

        self._completar_recursivo(nodo.enlace, objetivo, actual_indice + 1)

    def obtener_lista(self):
        lista = []
        self._llenar_lista(self.inicio, lista, 0)
        return lista

    def _llenar_lista(self, nodo, lista, indice):
        if nodo is None:
            return

        estado = "[x]" if nodo.completada else "[ ]"
        lista.append(f"{indice}. {estado} {nodo.contenido}")

        self._llenar_lista(nodo.enlace, lista, indice + 1)

class App:
    def __init__(self, root):
        self.lista = CadenaTareas()

        self.root = root
        self.root.title("Gestor de Tareas (Seleccionable)")

        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=10)

        self.boton = tk.Button(root, text="Agregar tarea", command=self.agregar_tarea)
        self.boton.pack(pady=5)

        self.boton_completar = tk.Button(root, text="Completar tarea seleccionada", command=self.completar_tarea)
        self.boton_completar.pack(pady=5)

        self.lista_visual = tk.Listbox(root, width=50, height=15)
        self.lista_visual.pack(pady=10)

    def agregar_tarea(self):
        texto = self.entrada.get()

        if texto != "":
            self.lista.agregar(texto)
            self.actualizar()
            self.entrada.delete(0, tk.END)

    def completar_tarea(self):
        seleccion = self.lista_visual.curselection()

        if seleccion:
            indice = seleccion[0]
            self.lista.completar(indice)
            self.actualizar()

    def actualizar(self):
        self.lista_visual.delete(0, tk.END)
        datos = self.lista.obtener_lista()
        self._insertar_recursivo(datos, 0)

    def _insertar_recursivo(self, datos, indice):
        if indice >= len(datos):
            return

        self.lista_visual.insert(tk.END, datos[indice])
        self._insertar_recursivo(datos, indice + 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()