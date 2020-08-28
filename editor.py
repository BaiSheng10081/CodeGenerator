import tkinter as tk
from tkinter import ttk

import suggest

class EditorWindow(tk.Frame):
    def __init__(self):
        self.parent = tk.Tk()
        super(EditorWindow, self).__init__(self.parent)

        self.parent.title("Editor - Untitled")
        self.parent.geometry("800x600")

        suggestWin = suggest.SuggestWindow()

        self.parent.mainloop()
