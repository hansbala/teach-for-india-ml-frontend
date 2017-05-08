#!/usr/bin/python
#TFI CODING PLATFORM
#WINDOWS
#Test Bench - Windows 10 64 bit - Python 2.7.11

from Tkinter import *
import os

##############################################################
# GLOBAL VARIABLES
##############################################################
path = "C:\\TFIpy\\"
#For the Next Button Actions
key = 1 #Defaults to syntax
pos = 1 #Defaults to the welcome message
res = ""
num_in_syntax = 9
num_in_string = 10
num_in_cond = 9
num_in_func = 5
num_in_loops = 7
values = [0, num_in_syntax, num_in_string, num_in_cond, num_in_func, num_in_loops]
syns = ['','welc','var','bool','spc','inter','com','mat','expo','mod']
strin = ['','strns','esc','ind','low','upp','str','dotnot','ps','pv','concat','format']
cond = ['','flow','comp','and','or','not','mix_match','cond_syn','if_else','big_if']
func = ['','func','call_res','func_call_func','par_args','imports']
loop = ['','loop','while','for','infi','break','cont','for_over_lists']
##############################################################

###############################################################
# ON CLICK BUTTON / MENU ACTIONS
###############################################################
def onClickMenuButton(st, i):
	global key, pos, syns, strin, cons, func, loop, res
	pos = i
	text1.config(state="normal")
	if (st=="syntax"):
		res = syns[i]
		key = 1
	elif (st=="string"):
		res = strin[i]
		key = 2
	elif (st=="conditionals"):
		res = cond[i]
		key = 3
	elif (st=="functions"):
		res = func[i]
		key = 4
	elif (st=="loops"):
		res = loop[i]
		key = 5
	text1.delete("1.0", END)
	info_file = open(path+res+".txt")
	info = info_file.read()
	info_file.close()
	text1.insert(END, info);
	text1.config(state="disabled")
def goNext():
	#Tells the interpreter that key and pos are infact global varibales
	#and does not confuse the interpreter that the assignment of key
	#and pos variabes are not to be treated as local.
	global key, pos
	if (pos < values[key]):
		pos += 1 #Goto next page under same menu
	else:
		if (key == 5):
			#If we reach end, default to the welcome page
			key=1
			pos=1
		else:
			#We go to the next menu - 1st page.
			key += 1
			pos = 1
	#Call the respective view function
	if (key==1):
		onClickMenuButton("syntax", pos)
	elif (key==2):
		onClickMenuButton("string", pos)
	elif (key==3):
		onClickMenuButton("conditionals", pos)
	elif (key==4):
		onClickMenuButton("functions", pos)
	elif (key==5):
		onClickMenuButton("loops", pos)
def goPrevious():
	#Tells the interpreter that key and pos are infact global varibales
	#and does not confuse the interpreter that the assignment of key
	#and pos variabes are not to be treated as local.
	global key, pos
	pass;

def goToPage1():
	global key, pos
	text1.config(state="normal")
	key=1
	pos=1
	onClickMenuButton("syntax", pos)
	text1.config(state="disabled")
#Save the Python code into C:\TFIpy\text.py
#and display it in a command window
def save():
    open((path+"text.py"),"w").close()
    text = text2.get("1.0",'end-1c')
    with open((path+"text.py"), "a") as f:
        f.write(text)
    run();
#run the Python code from C:\TFIpy\text.py
#and display it in a cmd window
def run():
    os.system("python -i "+path+"text.py")
def clearText():
	text2.delete("1.0", END)
########################################################
########################################################

#######################################################
#Main starts below
#######################################################
if not os.path.exists('C:\\TFIpy\\'):
	os.makedirs('C:\\TFIpy\\')
root = Tk()
root.state('zoomed')
root.configure(background='black')
root.wm_title("TFI Coding Platform")
root.iconbitmap("C:\\TFIpy\\logo.ico")

#Creating the paned window which holds the two text boxes
m = PanedWindow(root)
m.pack(fill=BOTH, expand=1)

#Creating Left Text Box which holds coding info....
#text1 = Text(m, height=15, width=52, bg="#add8e6", wrap=WORD, font=("bariol",17))
text1 = Text(m, height=15, width=52, bg="#add8e6", wrap=WORD, font=("verdana",15))
m.add(text1)
#text1.config(state="disabled")

#Creating right text box - Python editor window
#text2 = Text(m, height=15, width=50, bg="#354551", fg="#A8B265", wrap=WORD, font=("menlo", 15))
text2 = Text(m, height=15, width=50, bg="#354551", fg="#A8B265", wrap=WORD, font=("verdana", 15))
m.add(text2)

#Making the toolbar which holds the 'EXECUTE' and 'NEXT' buttons
toolbar = Frame(root)
#Creating the execute button
execu = Button(toolbar, text="SAVE & EXECUTE", width=15, command=save)
execu.pack(side=RIGHT, padx=2, pady=2)

#Creating MAIN PAGE' button
main_page = Button(toolbar, text="BACK TO MAIN PAGE", width=20, command=goToPage1)
main_page.pack(side=LEFT, padx=2, pady=2)

#Creating the PREVIOUS Button
prev = Button(toolbar, text="PREVIOUS", width=13, command=goPrevious)
prev.pack(side=LEFT, padx=2, pady=2)

#Creating the Next Button
nex = Button(toolbar, text="NEXT", width=9, command=goNext)
nex.pack(side=LEFT, padx=2, pady=2)

#Creating the clear button
clearme = Button(toolbar, text="CLEAR", width=9, command=clearText)
clearme.pack(side=RIGHT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

##################################################
#Creating a menu bar which holds the various
#topics to be learnt
##################################################
##################################################
menubar = Menu(root)
#'Syntax' Menu
syntaxMenu = Menu(menubar, tearoff=0)
syntaxMenu.add_command(label="WELCOME", command=lambda : onClickMenuButton("syntax",1))
syntaxMenu.add_command(label="VARIABLES", command=lambda : onClickMenuButton("syntax", 2))
syntaxMenu.add_command(label="BOOLEANS", command=lambda : onClickMenuButton("syntax", 3))
syntaxMenu.add_command(label="WHITESPACE",command=lambda : onClickMenuButton("syntax", 4))
syntaxMenu.add_command(label="INTERPRETATION", command=lambda : onClickMenuButton("syntax", 5))
syntaxMenu.add_command(label="COMMENTS", command=lambda : onClickMenuButton("syntax", 6))
syntaxMenu.add_command(label="MATHS", command=lambda : onClickMenuButton("syntax", 7))
syntaxMenu.add_command(label="EXPONENTIATION", command=lambda : onClickMenuButton("syntax", 8))
syntaxMenu.add_command(label="MODULO", command=lambda : onClickMenuButton("syntax", 9))
syntaxMenu.add_separator()
syntaxMenu.add_command(label="EXIT", command=root.quit)
menubar.add_cascade(label="SYNTAX", menu=syntaxMenu)

#'String & output' Menu
stringMenu = Menu(menubar, tearoff=0)
stringMenu.add_command(label="STRINGS", command=lambda : onClickMenuButton("string", 1))
stringMenu.add_command(label="ESCAPING", command=lambda : onClickMenuButton("string", 2))
stringMenu.add_command(label="INDEXATION", command=lambda : onClickMenuButton("string", 3))
stringMenu.add_command(label="STRING METHODS AND LOWER()", command=lambda : onClickMenuButton("string", 4))
stringMenu.add_command(label="UPPER()", command=lambda : onClickMenuButton("string", 5))
stringMenu.add_command(label="STR()", command=lambda : onClickMenuButton("string", 6))
stringMenu.add_command(label="DOT NOTATION", command=lambda : onClickMenuButton("string", 7))
stringMenu.add_command(label="PRINTING STRINGS", command=lambda : onClickMenuButton("string", 8))
stringMenu.add_command(label="PRINTING VARIABLES", command=lambda : onClickMenuButton("string", 9))
stringMenu.add_command(label="CONCATENATION", command=lambda : onClickMenuButton("string", 10))
#stringMenu.add_command(label="% FORMATTING", command=lambda : onClickMenuButton("string", 11))
menubar.add_cascade(label="STRINGS & OUTPUT", menu=stringMenu)
#'conditionals and control flow' menu
condMenu = Menu(menubar, tearoff=0)
condMenu.add_command(label="FLOW", command = lambda : onClickMenuButton("conditionals", 1))
condMenu.add_command(label="COMPARE", command = lambda : onClickMenuButton("conditionals", 2))
condMenu.add_command(label="AND", command = lambda : onClickMenuButton("conditionals", 3))
condMenu.add_command(label="OR", command = lambda : onClickMenuButton("conditionals", 4))
condMenu.add_command(label="NOT", command = lambda : onClickMenuButton("conditionals", 5))
condMenu.add_command(label="MIX & MATCH", command = lambda : onClickMenuButton("conditionals", 6))
condMenu.add_command(label="CONDITIONAL SYNTAX", command = lambda : onClickMenuButton("conditionals", 7))
condMenu.add_command(label="IF-ELSE", command = lambda : onClickMenuButton("conditionals", 8))
condMenu.add_command(label="THE BIG IF", command = lambda : onClickMenuButton("conditionals", 9))
menubar.add_cascade(label="CONDITIONALS", menu=condMenu)
#'Functions' menu
funcMenu = Menu(menubar, tearoff=0)
funcMenu.add_command(label="FUNCTIONS", command=lambda : onClickMenuButton("functions", 1))
funcMenu.add_command(label="CALL & RESPONSE", command=lambda : onClickMenuButton("functions", 2))
funcMenu.add_command(label="FUNC CALLING FUNC", command=lambda : onClickMenuButton("functions", 3))
funcMenu.add_command(label="PARAMS AND ARGS", command=lambda : onClickMenuButton("functions", 4))
funcMenu.add_command(label="IMPORTS", command=lambda : onClickMenuButton("functions", 5))
menubar.add_cascade(label="FUNCTIONS", menu=funcMenu)
#'Loops' menu
loopMenu = Menu(menubar, tearoff=0)
loopMenu.add_command(label="LOOPS", command=lambda : onClickMenuButton("loops", 1))
loopMenu.add_command(label="WHILE", command=lambda : onClickMenuButton("loops", 2))
loopMenu.add_command(label="FOR", command=lambda : onClickMenuButton("loops", 3))
loopMenu.add_command(label="INFINITE",command=lambda : onClickMenuButton("loops", 4))
loopMenu.add_command(label="BREAK", command=lambda : onClickMenuButton("loops", 5))
loopMenu.add_command(label="CONTINUE", command=lambda : onClickMenuButton("loops", 6))
loopMenu.add_command(label="FOR OVER LISTS", command=lambda : onClickMenuButton("loops", 7))
menubar.add_cascade(label="LOOPS", menu=loopMenu)

#Display the welcome message initially.
onClickMenuButton("syntax", 1)
root.config(menu=menubar)
root.mainloop()
################################################################
#%%%%%%%%%%%%%%%%%%%%%%%% END MAIN %%%%%%%%%%%%%%%%%%%%%%%%%%%%#