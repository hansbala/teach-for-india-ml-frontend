"""
import Tkinter as tki # Tkinter -> tkinter in Python3

class App(object):

    def __init__(self):
        self.root = tki.Tk()

    # create a Frame for the Text and Scrollbar
        txt_frm = tki.Frame(self.root, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tki.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

app = App()
app.root.mainloop()
from Tkinter import *
root = Tk()
root.state('zoomed')

m = PanedWindow(root)
m.pack(fill=BOTH, expand=1)

#Left Frame
txt_frm1 = Frame(m, height=16, width=634567890876543252)
txt_frm1.pack(fill=BOTH, expand=True)
txt_frm1.grid_propagate(True)
txt_frm1.grid_rowconfigure(0, weight=1)
txt_frm1.grid_columnconfigure(0, weight=1)
m.add(txt_frm1)
text1 = Text(txt_frm1, height=15, width=51)
text1.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
scrollb = Scrollbar(txt_frm1, command=text1.yview)
scrollb.grid(row=0, column=1, sticky="nsew")
text1['yscrollcommand'] = scrollb.set

#Right Frame
txt_frm2 = Frame(m, height=16, width=52)
txt_frm2.pack(fill=BOTH, expand=False)
txt_frm2.grid_propagate(False)
txt_frm2.grid_rowconfigure(0, weight=1)
txt_frm2.grid_columnconfigure(0, weight=1)
m.add(txt_frm2)
text2=Text(txt_frm2, height=15, width=49)
text2.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
scrollb2 = Scrollbar(txt_frm2, command=text2.yview)
scrollb2.grid(row=0, column=1, sticky="nsew")
text2['yscrollcommand'] = scrollb2.set

root.mainloop()
"""