from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename
import collections
import re


file_str = ""  # Globale Variable, um den Inhalt der eingelesenen Datei zu speichern

def textFileReader(label_pfad, frm):
    global file_str
    selected_file = askopenfilename(title="Datei wählen", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if selected_file:
        label_pfad.config(text="Datei-Pfad: " + selected_file)   
        with open(selected_file, 'r', encoding='utf-8') as f:
            file_str = f.read()
        print(type(file_str))
    else:
        label_pfad.config(text="Datei-Pfad: (keine Datei gewählt)")
        

wortliste = []
wortliste_gezaehlt = collections.Counter()

def countWords(tree):   # Anzahl der Häufigkeit der Wörter zählen
    
    tree.delete(*tree.get_children())
    wortliste.clear()
    wortliste_gezaehlt.clear()

    words = [re.sub(r"[^\wäöüÄÖÜß]", "", word.lower()) for word in file_str.split()]
    words = [word for word in words if word]

    wortliste.extend(words)
    wortliste_gezaehlt.update(wortliste)

    for idx, (word, count) in enumerate(wortliste_gezaehlt.most_common(), start=1):
        tree.insert("", "end", iid=f"item{idx}", values=(count, word))

    



   