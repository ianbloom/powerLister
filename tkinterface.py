"""
Users will be asked to select a .csv from accounts portal.

Then, they will be asked to select the instance name and the column of values they would like to extract.

They will be asked to specify a Salesforce contact report (containing account site trimmed)

They will be asked to specify the column containing account site trimmed by header

Then, the user will be asked to specify the header for the data to be imported from the accounts level report


"""
from tkinter import *
from tkinter import filedialog

###
###
###
###
###

def fileOpener():
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select CSV file",filetypes = (("csv files","*.csv"),("all files","*.*")))
	return(root.filename)

###
###
###
###
###
 
root = Tk()
root.title("Gainsight Contact List Creator")

label = Label(root,text="Please select an accounts portal report")
label.grid(row=0, column=0)

b = Button(root, text="OK", command=fileOpener)
b.grid(row=1, column=0)

label2 = Label(root,text="Please select a Salesforce Contacts report")
label2.grid(row=2, column=0)

c = Button(root, text="OK", command=fileOpener)
c.grid(row=3, column=0)

label3 = Label(root,text="Please select the Instance column")
label3.grid(row=4, column=0)

idvar = StringVar(root)
idvar.set("one")
idMenu = OptionMenu(root, idvar, "one", "two", "three")
idMenu.grid(row=5, column=0)

label4 = Label(root,text="Please select column you would like to condition")
label4.grid(row=6, column=0)

valvar = StringVar(root)
valvar.set("one")
valMenu = OptionMenu(root, valvar, "one", "two", "three")
valMenu.grid(row=7, column=0)

label5 = Label(root,text="Please select a conditional operator")
label5.grid(row=8, column=0)

convar = StringVar(root)
convar.set("<")
operatorMenu = OptionMenu(root, convar, "<", ">", "=", "!=")
operatorMenu.grid(row=9, column=0)

label6 = Label(root,text="Please enter a conditional value")
label6.grid(row=10, column=0)

e = Entry(root)
e.grid(row=11, column=0)

label6 = Label(root,text="Please name your new .csv file")
label6.grid(row=12, column=0)

f = Entry(root)
f.grid(row=13, column=0)

r = Button(root, text="RUN", command=fileOpener)
r.grid(row=14, column=0)

root.mainloop()