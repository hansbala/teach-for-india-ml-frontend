#FOR WINDOWS
from Tkinter import *
import os

##############################################################
# GLOBAL VARIABLES
##############################################################
path = "C:\\TFIpy\\"
#For the Next Button Actions
key = 1 #Defaults to syntax
pos = 1 #Defaults to the welcome message
num_in_syntax = 9
num_in_string = 10
num_in_cond = 9
num_in_func = 5
num_in_loops = 7
values = [0, num_in_syntax, num_in_string, num_in_cond, num_in_func, num_in_loops]
##############################################################

###############################################################
# ON CLICK BUTTON / MENU ACTIONS
###############################################################
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
		onClickSyntax(pos)
	elif (key==2):
		onClickString(pos)
	elif (key==3):
		onClickCond(pos)
	elif (key==4):
		onClickFunc(pos)
	else:
		onClickLoop(pos)
def goToPage1():
	global key, pos
	key=1
	pos=1
	onClickSyntax(pos)
def onClickSyntax(i):
	global key, pos
	key = 1
	pos = i
	text1.config(state="normal")
	syns = ['','welc','var','bool','spc','inter','com','mat','expo','mod']
	res = syns[i]
	text1.delete("1.0", END)
	info_file = open(path+res+".txt")
	info = info_file.read()
	info_file.close()
	text1.insert(END, info);
	text1.config(state="disabled")
def onClickString(i):
	global key, pos
	key = 2
	pos = i
	text1.config(state="normal")
	strin = ['','strns','esc','ind','low','upp','str','dotnot','ps','pv','concat','format']
	res = strin[i]
	text1.delete("1.0", END)
	info_file = open(path+res+".txt")
	info = info_file.read()
	info_file.close()
	text1.insert(END, info);
	text1.config(state="disabled")
def onClickCond(i):
	global key, pos
	key = 3
	pos = i
	text1.config(state="normal")
	cond = ['','flow','comp','and','or','not','mix_match','cond_syn','if_else','big_if']
	res = cond[i]
	text1.delete("1.0", END)
	info_file = open(path+res+".txt")
	info = info_file.read()
	info_file.close()
	text1.insert(END, info);
	text1.config(state="disabled")
def onClickFunc(i):
	global key, pos
	key = 4
	pos = i
	text1.config(state="normal")
	func = ['','func','call_res','func_call_func','par_args','imports']
	res = func[i]
	text1.delete("1.0", END)
	info_file = open(path+res+".txt")
	info = info_file.read()
	info_file.close()
	text1.insert(END, info);
	text1.config(state="disabled")
def onClickLoop(i):
	key = 5
	pos = i
	global key, pos
	text1.config(state="normal")
	loop = ['','loop','while','for','infi','break','cont','for_over_lists']
	res = loop[i]
	text1.delete("1.0", END)
	info_file = open(path+res+".txt")
	info = info_file.read()
	info_file.close()
	text1.insert(END, info);
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
text1 = Text(m, height=15, width=52, bg="#add8e6", wrap=WORD, font=("bariol",17))
m.add(text1)
data_file = open("print.txt")
data = data_file.read()
data_file.close()
text1.insert(END, data);
#text1.config(state="disabled")

#Creating right text box - Python editor window
text2 = Text(m, height=15, width=50, bg="#354551", fg="#A8B265", wrap=WORD, font=("menlo", 15))
m.add(text2)

#Making the toolbar which holds the 'EXECUTE' and 'NEXT' buttons
toolbar = Frame(root)
#Creating the execute button
execu = Button(toolbar, text="SAVE & EXECUTE", width=15, command=save)
execu.pack(side=RIGHT, padx=2, pady=2)

#Creating MAIN PAGE' button
main_page = Button(toolbar, text="BACK TO MAIN PAGE", width=20, command=goToPage1)
main_page.pack(side=LEFT, padx=2, pady=2)

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
syntaxMenu.add_command(label="WELCOME", command=lambda : onClickSyntax(1))
syntaxMenu.add_command(label="VARIABLES", command=lambda : onClickSyntax(2))
syntaxMenu.add_command(label="BOOLEANS", command=lambda : onClickSyntax(3))
syntaxMenu.add_command(label="WHITESPACE",command=lambda : onClickSyntax(4))
syntaxMenu.add_command(label="INTERPRETATION", command=lambda : onClickSyntax(5))
syntaxMenu.add_command(label="COMMENTS", command=lambda : onClickSyntax(6))
syntaxMenu.add_command(label="MATHS", command=lambda : onClickSyntax(7))
syntaxMenu.add_command(label="EXPONENTIATION", command=lambda : onClickSyntax(8))
syntaxMenu.add_command(label="MODULO", command=lambda : onClickSyntax(9))
syntaxMenu.add_separator()
syntaxMenu.add_command(label="EXIT", command=root.quit)
menubar.add_cascade(label="SYNTAX", menu=syntaxMenu)
#'String & output' Menu
stringMenu = Menu(menubar, tearoff=0)
stringMenu.add_command(label="STRINGS", command=lambda : onClickString(1))
stringMenu.add_command(label="ESCAPING", command=lambda : onClickString(2))
stringMenu.add_command(label="INDEXATION", command=lambda : onClickString(3))
stringMenu.add_command(label="STRING METHODS AND LOWER()", command=lambda : onClickString(4))
stringMenu.add_command(label="UPPER()", command=lambda : onClickString(5))
stringMenu.add_command(label="STR()", command=lambda : onClickString(6))
stringMenu.add_command(label="DOT NOTATION", command=lambda : onClickString(7))
stringMenu.add_command(label="PRINTING STRINGS", command=lambda : onClickString(8))
stringMenu.add_command(label="PRINTING VARIABLES", command=lambda : onClickString(9))
stringMenu.add_command(label="CONCATENATION", command=lambda : onClickString(10))
#stringMenu.add_command(label="% FORMATTING", command=lambda : onClickString(11))
menubar.add_cascade(label="STRINGS & OUTPUT", menu=stringMenu)
#'conditionals and control flow' menu
condMenu = Menu(menubar, tearoff=0)
condMenu.add_command(label="FLOW", command=lambda : onClickCond(1))
condMenu.add_command(label="COMPARE", command=lambda : onClickCond(2))
condMenu.add_command(label="AND", command=lambda : onClickCond(3))
condMenu.add_command(label="OR", command=lambda : onClickCond(4))
condMenu.add_command(label="NOT", command=lambda : onClickCond(5))
condMenu.add_command(label="MIX & MATCH", command=lambda : onClickCond(6))
condMenu.add_command(label="CONDITIONAL SYNTAX", command=lambda : onClickCond(7))
condMenu.add_command(label="IF-ELSE", command=lambda : onClickCond(8))
condMenu.add_command(label="THE BIG IF", command=lambda : onClickCond(9))
menubar.add_cascade(label="CONDITIONALS", menu=condMenu)
#'Functions' menu
funcMenu = Menu(menubar, tearoff=0)
funcMenu.add_command(label="FUNCTIONS", command=lambda : onClickFunc(1))
funcMenu.add_command(label="CALL & RESPONSE", command=lambda : onClickFunc(2))
funcMenu.add_command(label="FUNC CALLING FUNC", command=lambda : onClickFunc(3))
funcMenu.add_command(label="PARAMS AND ARGS", command=lambda : onClickFunc(4))
funcMenu.add_command(label="IMPORTS", command=lambda : onClickFunc(5))
menubar.add_cascade(label="FUNCTIONS", menu=funcMenu)
#'Loops' menu
loopMenu = Menu(menubar, tearoff=0)
loopMenu.add_command(label="LOOPS", command=lambda : onClickLoop(1))
loopMenu.add_command(label="WHILE", command=lambda : onClickLoop(2))
loopMenu.add_command(label="FOR", command=lambda : onClickLoop(3))
loopMenu.add_command(label="INFINITE",command=lambda : onClickLoop(4))
loopMenu.add_command(label="BREAK", command=lambda : onClickLoop(5))
loopMenu.add_command(label="CONTINUE", command=lambda : onClickLoop(6))
loopMenu.add_command(label="FOR OVER LISTS", command=lambda : onClickLoop(7))
menubar.add_cascade(label="LOOPS", menu=loopMenu)
#Display the welcome message initially.
onClickSyntax(1)
root.config(menu=menubar)
root.mainloop()
################################################################
#%%%%%%%%%%%%%%%%%%%%%%%% END MAIN %%%%%%%%%%%%%%%%%%%%%%%%%%%%#