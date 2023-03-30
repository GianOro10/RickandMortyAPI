import requests
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Rick and Morty API Search")
        self.geometry("600x400")

        # Create search bar
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.search_characters)
        self.search_entry = ttk.Entry(self, textvariable=self.search_var)
        self.search_entry.pack(pady=10)

        # Create character list
        self.character_listbox = tk.Listbox(self)
        self.character_listbox.pack(fill=tk.BOTH, expand=True)

        # Create character details frame
        self.character_details_frame = tk.Frame(self)
        self.character_details_frame.pack(fill=tk.BOTH, expand=True)

        # Create animations
        self.animation_canvas = tk.Canvas(self, bg="white", height=100)
        self.animation_canvas.pack(fill=tk.X)

        # Load characters
        self.characters = []
        self.load_characters()

    def load_characters(self):
        response = requests.get("https://rickandmortyapi.com/api/character")
        data = response.json()
        self.characters = data["results"]

        # Populate character list
        self.character_listbox.delete(0, tk.END)
        for character in self.characters:
            self.character_listbox.insert(tk.END, character["name"])

    def search_characters(self, *args):
        search_term = self.search_var.get()

        if search_term:
            response = requests.get(
                f"https://rickandmortyapi.com/api/character/?name={search_term}")
            data = response.json()
            self.characters = data["results"]
        else:
            self.load_characters()

        # Populate character list
        self.character_listbox.delete(0, tk.END)
        for character in self.characters:
            self.character_listbox.insert(tk.END, character["name"])

    def show_character_details(self, event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            index = selection[0]
            character = self.characters[index]

            # Clear character details frame
            for child in self.character_details_frame.winfo_children():
                child.destroy()

            # Populate character details frame
            for key, value in character.items():
                label = tk.Label(self.character_details_frame,
                                 text=f"{key.capitalize()}:")
                label.grid(sticky="W")
                label = tk.Label(self.character_details_frame, text=value)
                label.grid(row=self.character_details_frame.grid_size()[
                           1]-1, column=1, sticky="W")

    def run(self):
        self.mainloop()


app = App()
app.run()
