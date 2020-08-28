import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Frame):
    def __init__(self):
        self.parent = tk.Tk()
        super(MainWindow, self).__init__(self.parent)

        self.parent.title("Code Builder")
        self.parent.geometry("400x550")

        part1 = tk.Frame(self)

        self.searchBox = tk.Entry(part1)
        self.searchBox.pack(fill=tk.X , expand=True, side=tk.LEFT)

        self.searchBtn = tk.Button(part1, text="Search")
        self.searchBtn.pack(side=tk.RIGHT)

        part1.pack(fill=tk.X)

        self.searchSuggest = tk.Listbox(self)
        self.searchSuggest.pack(fill=tk.BOTH)


        self.pack(fill="both", expand=True, padx = 4, pady = 4)
        self.parent.mainloop()



def main():
    print("running... ")

    window = MainWindow()


if __name__ == "__main__":
    print("starting main progress")
    main()
