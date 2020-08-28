import tkinter as tk
from tkinter import ttk

import suggest
import editor

def main():
    print("running... ")
    suggest.load_file("./assets/database.json")

    editorWin = editor.EditorWindow()

if __name__ == "__main__":
    print("starting main progress")
    main()
