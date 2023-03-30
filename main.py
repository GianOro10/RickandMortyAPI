import requests
import tkinter as tk

BASE_URL = "https://rickandmortyapi.com/api/"


def search_characters(name):
    """
    Realiza una búsqueda de personajes en la API de Rick and Morty
    a partir del nombre y devuelve una lista de resultados.
    """
    url = BASE_URL + "character"
    params = {"name": name}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        return []


def create_gui():
    """
    Crea la interfaz gráfica de la aplicación.
    """
    # Crear la ventana principal
    window = tk.Tk()
    window.title("Rick and Morty API Search")

    # Crear la barra de búsqueda
    search_frame = tk.Frame(window)
    search_frame.pack(side=tk.TOP, padx=10, pady=10)

    search_label = tk.Label(search_frame, text="Nombre del personaje:")
    search_label.pack(side=tk.LEFT)

    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side=tk.LEFT)

    search_button = tk.Button(search_frame, text="Buscar",
                              command=lambda: search_callback(search_entry.get()))
    search_button.pack(side=tk.LEFT)

    # Crear el marco para mostrar los resultados
    results_frame = tk.Frame(window)
    results_frame.pack(side=tk.TOP, padx=10, pady=10)

    results_label = tk.Label(results_frame, text="Resultados de la búsqueda:")
    results_label.pack(side=tk.TOP)

    results_listbox = tk.Listbox(results_frame, width=50, height=10)
    results_listbox.pack(side=tk.TOP)

    # Función de devolución de llamada para la búsqueda
    def search_callback(name):
        results = search_characters(name)
        results_listbox.delete(0, tk.END)
        for result in results:
            results_listbox.insert(tk.END, result["name"])

    # Mostrar la ventana principal
    window.mainloop()


if __name__ == "__main__":
    create_gui()
