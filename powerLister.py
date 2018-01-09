"""
Users will be asked to select a .csv from accounts portal.

Then, they will be asked to select the instance name and the column of values they would like to extract.

They will be asked to specify a Salesforce contact report (containing account site trimmed)

They will be asked to specify the column containing account site trimmed by header

Then, the user will be asked to specify the header for the data to be imported from the accounts level report


"""
from tkinter import *
from tkinter import filedialog
from csvFunc import *

###
###
###
###
###

def fileOpener():
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select CSV file",filetypes = (("csv files","*.csv"),("all files","*.*")))
	return(root.filename)

def accountsFileOpener():
	global accountsFileName
	global accountsHeaderDict

	accountsFileName = fileOpener()
	headerTest = csvLoader(accountsFileName)
	accountsHeaderDict = headerParse(headerTest)
	idMenu = OptionMenu(root, idvar, *accountsHeaderDict)
	idMenu.grid(row=5, column=0)

	valMenu = OptionMenu(root, valvar, *accountsHeaderDict)
	valMenu.grid(row=7, column=0)

	return 0


def salesforceFileOpener():
	global salesForceFileName
	global sfHeaderDict

	salesForceFileName = fileOpener()
	headerTest = csvLoader(salesForceFileName)
	sfHeaderDict = headerParse(headerTest)

	sfMenu = OptionMenu(root, sfvar, *sfHeaderDict)
	sfMenu.grid(row=9, column=0)


def headerPrinter():
	global accountsHeaderDict
	for item in accountsHeaderDict:
		print(item)

def runIt():
	global accountsFileName
	global salesForceFileName
	global accountsHeaderDict

	headerTest = csvLoader(accountsFileName)
	headerArray = headerParse(headerTest)

	idPair = idvar.get()
	idColumn = accountsHeaderDict[idPair]

	valuePair = valvar.get()
	valueColumn = accountsHeaderDict[valuePair]

	# file = csvLoader('accountsPortal.csv')
	file = csvLoader(accountsFileName)

	accountsDict = columnStrip(file, int(idColumn), int(valueColumn))

	# Here's where I'd have the user select the condition to apply to the dictionary to filter users

	###
	###
	### GET THE > AND THE 20 PROGRAMATICALLY
	###
	###

	conditionalVariable = convar.get()
	conditionalValue = float(e.get())

	accountsDict = dictDeleter(accountsDict, conditionalVariable, conditionalValue)

	# Here's where the user would select their salesforce .csv 
	SFfile = csvLoader(salesForceFileName)

	# Ask the user to name the newfile
	newFileName = f.get()
	newFileName += ".csv"
	newfile = csvWriter(newFileName)

	accountSiteTrimmed = sfvar.get()
	accountSiteColumn = sfHeaderDict[accountSiteTrimmed]

	# Ask the user to name their header, possibly before naming newfile?
	headerName = h.get()
	dictSearcher(accountsDict, SFfile, accountSiteColumn, newfile, headerName)

###
###
###
###
###

accountsFileName = ""
salesForceFileName = ""
accountsHeaderDict = {"NONE", "NONE"}
sfHeaderDict = {"NONE", "NONE"}
 
root = Tk()
root.title("Gainsight Contact List Creator")

label = Label(root,text="Please select an accounts portal report")
label.grid(row=0, column=0)

b = Button(root, text="OK", command=accountsFileOpener)
b.grid(row=1, column=0)

label2 = Label(root,text="Please select a Salesforce Contacts report")
label2.grid(row=2, column=0)

c = Button(root, text="OK", command=salesforceFileOpener)
c.grid(row=3, column=0)

label3 = Label(root,text="Please select the Instance column")
label3.grid(row=4, column=0)

idvar = StringVar(root)
idvar.set("NONE")
idMenu = OptionMenu(root, idvar, *accountsHeaderDict)
idMenu.grid(row=5, column=0)

label4 = Label(root,text="Please select column you would like to condition")
label4.grid(row=6, column=0)

valvar = StringVar(root)
valvar.set("NONE")
valMenu = OptionMenu(root, valvar, *accountsHeaderDict)
valMenu.grid(row=7, column=0)

label8 = Label(root,text="Please select the Account Site Trimmed column")
label8.grid(row=8, column=0)

sfvar = StringVar(root)
sfvar.set("NONE")
sfMenu = OptionMenu(root, sfvar, *sfHeaderDict)
sfMenu.grid(row=9, column=0)

label5 = Label(root,text="Please select a conditional operator")
label5.grid(row=10, column=0)

convar = StringVar(root)
convar.set("<")
operatorMenu = OptionMenu(root, convar, "<", ">", "=", "!=")
operatorMenu.grid(row=11, column=0)

label6 = Label(root,text="Please enter a conditional value")
label6.grid(row=12, column=0)

e = Entry(root)
e.grid(row=13, column=0)

label9 = Label(root,text="Please provide a header for the column of values")
label9.grid(row=14, column=0)

h = Entry(root)
h.grid(row=15, column=0)

label6 = Label(root,text="Please name your new .csv file")
label6.grid(row=16, column=0)

f = Entry(root)
f.grid(row=17, column=0)

r = Button(root, text="RUN", command=runIt)
r.grid(row=18, column=0)

root.mainloop()