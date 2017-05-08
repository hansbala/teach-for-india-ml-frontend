from Tkinter import *
root = Tk()

def hello():
    text1.delete("1.0",END);
    text1.insert(END, "hello");
def special(index):
    if index==1:
        text1.delete("1.0",END);
        text1.insert(END, "number 1");
    if index==2:
        text1.delete("1.0",END);
    text1.insert(END, "number 2");

menubar = Menu(root)
text1 = Text(root, height=15, width=52, bg="#add8e6", wrap=WORD, font=("bariol",17))
text1.pack(fill=BOTH, expand=1)
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=special(1))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=special(2))
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)

root.mainloop()
