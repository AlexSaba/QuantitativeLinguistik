from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename
import collections


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

def countWords():   #Anzahl der Häufigkeit der Wörter zählen
    for word in file_str.split(" "):
        wortliste.append(word.lower())  
    wortliste_gezaehlt.update(wortliste)  # Wörter zur Zählung hinzufügen 
    #for wort in wortliste_gezaehlt:        #Wörter mit gleicher Häufigkeit alpabetisch sortieren
     #   if wortliste_gezaehlt[wort] 

    #wortliste_gezaehlt
    #wortliste.sort(reverse=True, )
    #print(wortliste_gezaehlt)

   