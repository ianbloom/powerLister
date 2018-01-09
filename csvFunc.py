"""
This program will take two .csv files as input.

One .csv is a LogicMonitor device metric trends report from the accounts portal.

The other is a .csv file consisting of SF account contacts owned by a CSM.

The program will filter accounts from the LogicMonitor report based on user
defined criteria, then perform a VLOOKUP appending the selected metric to the
SF .csv file.

The program will finally produce a .csv file consisting of all contacts that fulfill
the account level critera filtered for in the first .csv file for use in Gainsight
as a Powerlist.
"""

from csv import *
from tkinter import *
from tkinter import filedialog

###
###
###
###
###

def csvLoader(csvFile):
	f = open(csvFile)
	thing = reader(f)
	return(thing)

def csvWriter(csvFile):
	f = open(csvFile, 'w')
	thing = writer(f)
	return(thing)

def fileOpener():
	root = Tk()
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
	return(root.filename)

def columnStrip(reader, idIndex, valIndex):
	returnColumns = {}
	headerSkipper = 0
	for row in reader:
		headerSkipper += 1
		if headerSkipper > 2:
			# Produce AccountSiteTrimmed for dictionary key
			if "_Sales-" in row[idIndex]:	
				key = row[idIndex].replace("_Sales-", "")
			if "_Customer Success-" in row[idIndex]:	
				key = row[idIndex].replace("_Customer Success-", "")
			# Grab average column for dictionary value
			value = row[valIndex]
			if('K' in value):
				temp = float(value.replace('K', '')) * 1000
				returnColumns[key] = temp
			else:
				returnColumns[key] = value
	for item in returnColumns:
		print(item, returnColumns[item])
	return(returnColumns)

def dictSearcher(dictionary, csvReader, keyColumn, csvWriter, newHeader):
	count = 0
	for row in csvReader:
		# Append newHeader as header for column of values
		if count < 1:
			row.append(newHeader)
		# Catch errors for columns at the end of SF reports
		if keyColumn > len(row) - 1:
			continue
		else:
			value = dictionary.get(row[keyColumn])
			# Append values for nonheader rows
			if count >= 1:
				row.append(value)
			# Only append values that exist in the dictionary lookup
			# Count < 1 is appended to be sure that headers are maintained
			if value not in (None, "") or count < 1:
				csvWriter.writerow(row)
		count += 1

def dictDeleter(dictionary, conditionalString, conditionalValue):
	newDict = {}
	for item in dictionary:
		# Depending on the conditional statement a user selects, a different comparison is used
		if(dictionary[item] == "No Data"):
			continue
		if(conditionalString=="<"):
			if(float(dictionary[item]) < conditionalValue):
				newDict[item] = dictionary[item]
		if(conditionalString==">"):
			if(float(dictionary[item]) > conditionalValue):
				newDict[item] = dictionary[item]
		if(conditionalString=="="):
			if(float(dictionary[item]) == conditionalValue):
				newDict[item] = dictionary[item]
		if(conditionalString=="!="):
			if(float(dictionary[item]) != conditionalValue):
				newDict[item] = dictionary[item]
	return newDict
"""
def headerParse(reader):
	headerArray = []
	for row in reader:
		rowLength = len(row)
		# Take the first row that is nonempty and populate headerArray with its items
		if row[0] not in (None, ""):
			for col, item in enumerate(row):
				headerArray.append([item, col])
			break
	return(headerArray)
"""
def headerParse(reader):
	headerDict = {}
	for row in reader:
		rowLength = len(row)
		if row[0] not in (None, ""):
			for col, item in enumerate(row):
				headerDict[item] = col
			break
	return(headerDict)

###
###
###
###
###

"""
headerTest = csvLoader('accountsPortal.csv')
headerArray = headerParse(headerTest)
# print headers for users to select the account site to trim, and the value they are searching for
for item in headerArray:
	print(item[0])

idColumn = 1
valueColumn = 7

file = csvLoader('accountsPortal.csv')

accountsDict = columnStrip(file, 1, 7)

# Here's where I'd have the user select the condition to apply to the dictionary to filter users
accountsDict = dictDeleter(accountsDict, ">", 20)

accountSiteColumn = 1

# Here's where the user would select their salesforce .csv 
SFfile = csvLoader('SFReport.csv')

# Ask the user to name the newfile
newfile = csvWriter('newfile.csv')

# Ask the user to name their header, possibly before naming newfile?
dictSearcher(accountsDict, SFfile, accountSiteColumn, newfile, 'test header')
"""

