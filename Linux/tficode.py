
#!/usr/bin/python
# TFI CODING PLATFORM
# OS: LINUX
# Test Bench - Ubuntu 16.04 LTS - Python 2.7.11+

from Tkinter import *
import os
import subprocess
##############################################################
# GLOBAL VARIABLES
##############################################################
#PATH
path = os.path.expanduser('~')+"/.tfipy/"
info_path = path+"InfoFiles/"
init_code_path = path+"InitialCode/"
ans_code_path = path+"FinalCode/"
#For the Next Button Actions
key = 0 #Defaults to start menu
pos = 1 #Defaults to the welcome message
res = ""
res2 = ""
res3 = ""
# On adding additional topics, modify the corresponding variables 
# below and add respective menu buttons

num_in_start = 2 #We ignore the credits and exit buttons
num_in_syntax = 12
num_in_string = 16
num_in_cond = 15
num_in_func = 19
num_in_loops = 19
##############################################################
values = [num_in_start, num_in_syntax, num_in_string, num_in_cond, num_in_func, num_in_loops]

###############################################################
# ON CLICK BUTTON / MENU ACTIONS
###############################################################
def onClickMenuButton(st, i):
    global key, pos, res#, syntax_info, strings_info, conditionals_info, functions_info, loops_info, res
    pos = i
    text1.config(state="normal")
    if (st=="syntax"):
        res = "Syntax/"+"less"+str(i+1)+".txt"
        res2 = "Syntax/"+"less"+str(i+1)+".py"
        key = 1
    elif (st=="string"):
        res = "Strings/"+"less"+str(i)+".txt"
        res2 = "Strings/"+"less"+str(i)+".py"
        key = 2
    elif (st=="conditionals"):
        res = "Conditionals/"+"less"+str(i)+".txt"
        res2 = "Conditionals/"+"less"+str(i)+".py"
        key = 3
    elif (st=="functions"):
        res = "Functions/"+"less"+str(i)+".txt"
        res2 = "Functions/"+"less"+str(i)+".py"
        key = 4
    elif (st=="loops"):
        res = "Loops/"+"less"+str(i)+".txt"
        res2 = "Loops/"+"less"+str(i)+".py"
        key = 5
    text1.delete("1.0", END)
    info_file = open(info_path+res)
    info = info_file.read()
    info_file.close()
    text1.insert(END, info);
    text1.config(state="disabled")
    #Doing the same for the editor window
    #--Showing initilal code
    text2.delete("1.0", END)
    info_file = open(init_code_path+res2)
    info = info_file.read()
    info_file.close()
    text2.insert(END, info);

def onClickStart(i):
    global res, key, pos
    key = 0
    pos = i
    text1.config(state="normal")
    text1.delete("1.0", END)
    if(i==1):
        res = "welc.txt"
    elif(i==2):
        res = "instructions.txt"
    info_file = open(info_path+res)
    info = info_file.read()
    info_file.close()
    text1.insert(END, info);
    text1.config(state="disabled")
    text2.delete("1.0", END)

def goNext():
    #Tells the interpreter that key and pos are infact global varibales
    #and does not confuse the interpreter that the assignment of key
    #and pos variabes are not to be treated as local.
    global key, pos
    if (pos < values[key]):
        pos += 1 #Goto next page under same menu
    else:
        if (key == 5):
            #If we reach end, stay on that page
            key=5
            pos=pos #For clarity
        else:
            #We go to the next menu - 1st page.
            key += 1
            pos = 1
    #Call the respective view function
    if (key==0):
        onClickStart(pos)
    elif (key==1):
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
    if (pos > 1):
        pos -= 1
    else:
        if (key==0):
            #If we are at the start, do not wrap around to the end
            key=0
            pos=pos
        else:
            key -= 1
            # For modifying respective inner topics, evaluate the 
            # number in each respective main topic
            if (key==0):
                pos = num_in_start
            elif (key==1):
                pos = num_in_syntax
            elif (key==2):
                pos = num_in_string
            elif(key==3):
                pos = num_in_cond
            elif(key==4):
                pos = num_in_func
            elif(key==5):
                pos = num_in_loops
    #Call the respective view function
    if (key==0):
        onClickStart(pos)
    elif (key==1):
        onClickMenuButton("syntax", pos)
    elif (key==2):
        onClickMenuButton("string", pos)
    elif (key==3):
        onClickMenuButton("conditionals", pos)
    elif (key==4):
        onClickMenuButton("functions", pos)
    elif (key==5):
        onClickMenuButton("loops", pos)

def showAnswer():
    #Aims to show the solution for the exercise
    #given on the page the user is currently looking at
    #Might use the 'key' and 'pos' global variables?????
    global res3
    global key, pos;
    if (key == 1):
        res3 = "Syntax/"+"less"+str(pos+1)+".py"
    elif (key == 2):
        res3 = "Strings/"+"less"+str(pos)+".py"
    elif (key == 3):
        res3 = "Conditionals/"+"less"+str(pos)+".py"
    elif (key == 4):
        res3 = "Functions/"+"less"+str(pos)+".py"
    elif (key == 5):
        res3 = "Loops/"+"less"+str(pos)+".py"
    
    try:
        text2.delete("1.0", END)
        info_file = open(ans_code_path+res3)
        info = info_file.read()
        info_file.close()
        text2.insert(END, info);
    except:
        pass
    
def goToPage1():
    global key, pos
    text1.config(state="normal")
    key=0
    pos=1
    onClickStart(1)
    text1.config(state="disabled")
    text2.delete("1.0", END)
def save():
    open((path+"text.py"),"w").close()
    text = text2.get("1.0",'end-1c')
    with open((path+"text.py"), "a") as f:
        f.write(text)
    run();
def run():
    #temp = "python -i "+ path + "text.py"
    #os.system("x-terminal-emulator; python -i "+path+"text.py")
    #subprocess.call(['gnome-terminal', '-x'])
    #subprocess.call(['gnome-terminal', '-x', 'python -i /home/hans/.tfipy/text.py'])
    os.system("gnome-terminal -x python -i " + path + "text.py")
def ResetCode():
    text2.delete("1.0", END)
def showCredits():
    text1.config(state="normal")
    text1.delete("1.0", END)
    info_file = open(info_path+"credits"+".txt")
    info = info_file.read()
    info_file.close()
    text1.insert(END, info)
    text1.config(state="disabled")
########################################################
########################################################

#######################################################
#Main starts below
#######################################################
root = Tk()
#root.state('zoomed')
root.attributes('-zoomed', True)
root.wm_title("TFI Coding Platform")
#root.iconbitmap(path+"logo.ico")

#Creating the paned window which holds the two text boxes
m = PanedWindow(root)
m.pack(fill=BOTH, expand=1)

#Creating Left Frame whcih holds Text Box and the scroll
#bar for coding info and instructions....
left_frame = Frame(m, height=15, width=652)
left_frame.pack(fill=BOTH, expand=True)
left_frame.grid_propagate(True)
left_frame.grid_rowconfigure(0, weight=1)
left_frame.grid_columnconfigure(0, weight=1)
m.add(left_frame)
text1 = Text(left_frame, height=15, width=52, bg="#add8e6", wrap=WORD, font=("verdana",15))
text1.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
sv1 = Scrollbar(left_frame, command=text1.yview)
sv1.grid(row=0, column=1, sticky="nsew")
text1['yscrollcommand'] = sv1.set

#Creating right text box - Python editor window
text2 = Text(m, height=15, width=50, bg="#354551", fg="#A8B265", wrap=WORD, font=("verdana", 15))
m.add(text2)


##############################################################################
#  BUTTONS ON BOTTOM TOOLBAR IN THE FOLLOWING ORDER:
#  |MAIN PAGE| |PREVIOUS| |NEXT|               |SHOW ANSWER| |CLEAR| |EXECUTE|
###############################################################################
#Making the toolbar which holds all the above buttons
toolbar = Frame(root)
#Creating MAIN PAGE' button
main_page = Button(toolbar, text="BACK TO MAIN PAGE", width=20, command=goToPage1)
main_page.pack(side=LEFT, padx=2, pady=2)
#Creating the PREVIOUS Button
prev = Button(toolbar, text="PREVIOUS", width=13, command=goPrevious)
prev.pack(side=LEFT, padx=2, pady=2)
#Creating the Next Button
nex = Button(toolbar, text="NEXT", width=9, command=goNext)
nex.pack(side=LEFT, padx=2, pady=2)
#Creating the execute button
execu = Button(toolbar, text="EXECUTE", width=15, command=save)
execu.pack(side=RIGHT, padx=2, pady=2)
#Creating the clear button
resetme = Button(toolbar, text="RESET", width=9, command=ResetCode)
resetme.pack(side=RIGHT, padx=2, pady=2)
#Creating the 'SHOW ANSWER' button
ansme = Button(toolbar, text="SHOW ANSWER", width=17, command=showAnswer)
ansme.pack(side=RIGHT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)
###########################################################################

##################################################
#Creating a menu bar which holds the various
#topics to be learnt
##################################################
menubar = Menu(root)
#Start Menu
starMenu = Menu(menubar, tearoff=0)
starMenu.add_command(label="WELCOME", command=lambda : onClickStart(1))
starMenu.add_command(label="INSTRUCTIONS", command=lambda : onClickStart(2))
starMenu.add_command(label="CREDITS", command=showCredits)
starMenu.add_command(label="EXIT", command=root.quit)
menubar.add_cascade(label="START", menu=starMenu)
#'Syntax' Menu
syntaxMenu = Menu(menubar, tearoff=0)
syntaxMenu.add_command(label="VARIABLES", command=lambda : onClickMenuButton("syntax", 1))
syntaxMenu.add_command(label="BOOLEANS", command=lambda : onClickMenuButton("syntax", 2))
syntaxMenu.add_command(label="REASSIGNMENT", command=lambda : onClickMenuButton("syntax", 3))
syntaxMenu.add_command(label="WHITESPACE",command=lambda : onClickMenuButton("syntax", 4))
syntaxMenu.add_command(label="INDENTATION ERRORS", command=lambda : onClickMenuButton("syntax", 5))
syntaxMenu.add_command(label="INTERPRETATION", command=lambda : onClickMenuButton("syntax", 6))
syntaxMenu.add_command(label="SINGLE COMMENTS", command=lambda : onClickMenuButton("syntax", 7))
syntaxMenu.add_command(label="MULTI COMMENTS", command=lambda : onClickMenuButton("syntax", 8))
syntaxMenu.add_command(label="MATH", command=lambda : onClickMenuButton("syntax", 9))
syntaxMenu.add_command(label="EXPONENTIATION", command=lambda : onClickMenuButton("syntax", 10))
syntaxMenu.add_command(label="MODULO", command=lambda : onClickMenuButton("syntax", 11))
syntaxMenu.add_command(label="ALL TOGETHER", command=lambda : onClickMenuButton("syntax", 12))
menubar.add_cascade(label="SYNTAX", menu=syntaxMenu)

#'String & output' Menu
stringMenu = Menu(menubar, tearoff=0)
stringMenu.add_command(label="STRINGS", command=lambda : onClickMenuButton("string", 1))
stringMenu.add_command(label="PRACTICE", command=lambda : onClickMenuButton("string", 2))
stringMenu.add_command(label="ESCAPING", command=lambda : onClickMenuButton("string", 3))
stringMenu.add_command(label="INDEXATION", command=lambda : onClickMenuButton("string", 4))
stringMenu.add_command(label="STRING METHODS", command=lambda : onClickMenuButton("string", 5))
stringMenu.add_command(label="LOWER()", command=lambda : onClickMenuButton("string", 6))
stringMenu.add_command(label="UPPER()", command=lambda : onClickMenuButton("string", 7))
stringMenu.add_command(label="STR()", command=lambda : onClickMenuButton("string", 8))
stringMenu.add_command(label="DOT NOTATION", command=lambda : onClickMenuButton("string", 9))
stringMenu.add_command(label="PRINTING STRINGS", command=lambda : onClickMenuButton("string", 10))
stringMenu.add_command(label="PRINTING VARIABLES", command=lambda : onClickMenuButton("string", 11))
stringMenu.add_command(label="CONCATENATION", command=lambda : onClickMenuButton("string", 12))
stringMenu.add_command(label="STRING CONVERSION", command=lambda : onClickMenuButton("string", 13))
stringMenu.add_command(label="FORMATTING I", command=lambda : onClickMenuButton("string", 14))
stringMenu.add_command(label="FORMATTING II", command=lambda : onClickMenuButton("string", 15))
stringMenu.add_command(label="STRING EXERCISE", command=lambda : onClickMenuButton("string", 16))
menubar.add_cascade(label="STRINGS & OUTPUT", menu=stringMenu)
#'conditionals and control flow' menu
condMenu = Menu(menubar, tearoff=0)
condMenu.add_command(label="FLOW", command = lambda : onClickMenuButton("conditionals", 1))
condMenu.add_command(label="COMPARE I", command = lambda : onClickMenuButton("conditionals", 2))
condMenu.add_command(label="COMPARE II", command = lambda : onClickMenuButton("conditionals", 3))
condMenu.add_command(label="TURNED TABLES", command = lambda : onClickMenuButton("conditionals", 4))
condMenu.add_command(label="AND/OR/NOT", command = lambda : onClickMenuButton("conditionals", 5))
condMenu.add_command(label="AND", command = lambda : onClickMenuButton("conditionals", 6))
condMenu.add_command(label="OR", command = lambda : onClickMenuButton("conditionals", 7))
condMenu.add_command(label="NOT", command = lambda : onClickMenuButton("conditionals", 8))
condMenu.add_command(label="THIS AND THAT", command = lambda : onClickMenuButton("conditionals", 9))
condMenu.add_command(label="MIX N MATCH", command = lambda : onClickMenuButton("conditionals", 10))
condMenu.add_command(label="CONDITIONAL SYNTAX", command = lambda : onClickMenuButton("conditionals", 11))
condMenu.add_command(label="IF", command = lambda : onClickMenuButton("conditionals", 12))
condMenu.add_command(label="ELSE", command = lambda : onClickMenuButton("conditionals", 13))
condMenu.add_command(label="SWITCH", command = lambda : onClickMenuButton("conditionals", 14))
condMenu.add_command(label="EXERCISE", command = lambda : onClickMenuButton("conditionals", 15))
menubar.add_cascade(label="CONDITIONALS", menu=condMenu)
#'Functions' menu
funcMenu = Menu(menubar, tearoff=0)
funcMenu.add_command(label="FUNCTIONS", command = lambda : onClickMenuButton("functions", 1))
funcMenu.add_command(label="FUNCTION JUNCTION", command = lambda : onClickMenuButton("functions", 2))
funcMenu.add_command(label="CALL AND RESPONSE", command = lambda : onClickMenuButton("functions", 3))
funcMenu.add_command(label="PARAMS AND ARGS", command = lambda : onClickMenuButton("functions", 4))
funcMenu.add_command(label="FUNC CALLING FUNC", command = lambda : onClickMenuButton("functions", 5))
funcMenu.add_command(label="PRACTICE", command = lambda : onClickMenuButton("functions", 6))
funcMenu.add_command(label="KUNG FU", command = lambda : onClickMenuButton("functions", 7))
funcMenu.add_command(label="GENERIC IMPORTS", command = lambda : onClickMenuButton("functions", 8))
funcMenu.add_command(label="FUNCTION IMPORTS", command = lambda : onClickMenuButton("functions", 9))
funcMenu.add_command(label="UNIVERSAL IMPORTS", command = lambda : onClickMenuButton("functions", 10))
funcMenu.add_command(label="DRAGONS", command = lambda : onClickMenuButton("functions", 11))
funcMenu.add_command(label="BEYOND STRINGS", command = lambda : onClickMenuButton("functions", 12))
funcMenu.add_command(label="MAX()", command = lambda : onClickMenuButton("functions", 13))
funcMenu.add_command(label="MIN()", command = lambda : onClickMenuButton("functions", 14))
funcMenu.add_command(label="ABS()", command = lambda : onClickMenuButton("functions", 15))
funcMenu.add_command(label="TYPE()", command = lambda : onClickMenuButton("functions", 16))
funcMenu.add_command(label="REVIEW", command = lambda : onClickMenuButton("functions", 17))
funcMenu.add_command(label="REVIEW: MODULES", command = lambda : onClickMenuButton("functions", 18))
funcMenu.add_command(label="REVIEW: BUILT IN", command = lambda : onClickMenuButton("functions", 19))
menubar.add_cascade(label="FUNCTIONS", menu=funcMenu)

#'Loops' menu
loopMenu = Menu(menubar, tearoff=0)
loopMenu.add_command(label="WHILE", command = lambda : onClickMenuButton("loops", 1))
loopMenu.add_command(label="CONDITION", command = lambda : onClickMenuButton("loops", 2))
loopMenu.add_command(label="WHILE II", command = lambda : onClickMenuButton("loops", 3))
loopMenu.add_command(label="SIMPLE ERRORS", command = lambda : onClickMenuButton("loops", 4))
loopMenu.add_command(label="INFINITE LOOPS", command = lambda : onClickMenuButton("loops", 5))
loopMenu.add_command(label="BREAK", command = lambda : onClickMenuButton("loops", 6))
loopMenu.add_command(label="WHILE-ELSE", command = lambda : onClickMenuButton("loops", 7))
loopMenu.add_command(label="PRACTICE", command = lambda : onClickMenuButton("loops", 8))
loopMenu.add_command(label="FOR I", command = lambda : onClickMenuButton("loops", 9))
loopMenu.add_command(label="FOR II", command = lambda : onClickMenuButton("loops", 10))
loopMenu.add_command(label="FOR III", command = lambda : onClickMenuButton("loops", 11))
loopMenu.add_command(label="FOR IV", command = lambda : onClickMenuButton("loops", 12))
loopMenu.add_command(label="FOR V", command = lambda : onClickMenuButton("loops", 13))
loopMenu.add_command(label="FOR DICTIONARIES", command = lambda : onClickMenuButton("loops", 14))
loopMenu.add_command(label="COUNTING", command = lambda : onClickMenuButton("loops", 15))
loopMenu.add_command(label="MULTIPLE LISTS", command = lambda : onClickMenuButton("loops", 16))
loopMenu.add_command(label="FOR-ELSE", command = lambda : onClickMenuButton("loops", 17))
loopMenu.add_command(label="EXERCISE: FOR I", command = lambda : onClickMenuButton("loops", 18))
loopMenu.add_command(label="EXERCISE: FOR II", command = lambda : onClickMenuButton("loops", 19))
menubar.add_cascade(label="LOOPS", menu=loopMenu)

#Display the welcome message initially.
onClickStart(1)
root.config(menu=menubar)
root.mainloop()
################################################################
#%%%%%%%%%%%%%%%%%%%%%%%% END MAIN %%%%%%%%%%%%%%%%%%%%%%%%%%%%#
