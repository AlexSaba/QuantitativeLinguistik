from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import filedialog as fd
from textFileReader import textFileReader
from textFileReader import countWords



root = Tk()
root.geometry('1000x600')

frm = ttk.Frame(root, padding=10)
frm.grid()

# Label mit Referenz speichern, damit wir es später aktualisieren können
label_pfad = ttk.Label(frm, text="Datei-Pfad: (keine Datei gewählt)")
label_pfad.grid(column=0, row=2, columnspan=10, sticky=W)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=10)
ttk.Button(frm, text="Datei öffnen", command=lambda: textFileReader(label_pfad, frm)).grid(column=0, row=1)
ttk.Button(frm, text="Wörter zählen", command=lambda: countWords(tree)).grid(column=2, row=10)

# Treeview
tree = ttk.Treeview(root, column=("c1", "c2"), show='headings', height=15)
#, x=530, y=60, height=100

# Scrollbar
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
vsb.place(in_=tree, relx=1.0, relheight=1.0, bordermode="inside")
tree.configure(yscrollcommand=vsb.set)

### listbox for directories
tree.column("# 1", anchor=CENTER, width=150)
tree.heading("# 1", text="Häufigkeit")
tree.column("# 2", anchor=CENTER, width=150)
tree.heading("# 2", text="Wort")
tree.grid(row=2, column=5, columnspan=7, padx=30, pady=30)

root.mainloop()