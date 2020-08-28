import tkinter as tk
from tkinter import ttk

import json

keywords = []
database = {}

class SuggestWindow(tk.Frame):
    def __init__(self, main=False):
        self.parent = tk.Toplevel()
        super(SuggestWindow, self).__init__(self.parent)

        self.parent.title("Suggestion")
        self.parent.geometry("200x350")

        part1 = tk.Frame(self)

        self.searchVariable = tk.StringVar()
        self.searchBox = tk.Entry(part1, textvariable=self.searchVariable)
        self.searchBox.pack(fill=tk.X , expand=True, side=tk.LEFT)

        self.searchBox.bind('<KeyRelease>', self.udpdateSuggestion)

        self.searchBtn = tk.Button(part1, text="Search")
        self.searchBtn.pack(side=tk.RIGHT)

        part1.pack(fill=tk.X)

        self.searchSuggest = tk.Listbox(self)
        self.searchSuggest.pack(fill=tk.BOTH, expand=True)

        self.pack(fill="both", expand=True, padx = 4, pady = 4)

    def udpdateSuggestion(self, event=None):
        values = self.searchVariable.get()

        self.searchSuggest.delete(0,'end')

        if(values.strip() == ""):
            return

        sugList = suggest_list(values)

        for item in sugList:
            self.searchSuggest.insert(tk.END, item)

def suggest_list(search):
    print(search)

    def searchKey(keyword):
        search.split(" ")

        w = 0
        for index, item in enumerate(search, start=1):
            w += (keyword.find(item)+1) * index

        print(w)
        return w
        

    suggestList = [n for n in keywords if n.find(search) > -1 and n[0] != "!" and n[0] != "@"]
    suggestList.sort(key=searchKey)

    return suggestList


def load_file(path):
    with open(path, 'r') as file:
        strings = ""
        for line in file.readlines():
            strings += line

        load(strings)


def load(string):
    global keywords, database
    jsonObj = json.loads(string)
    keywords = keywords + list(jsonObj.keys())
    database.update(jsonObj)

    print("data loaded")
