# powerLister
This program takes a .csv from the LogicMonitor accounts portal and a .csv of SalesForce Contacts as input.

The user is asked to select the instance column within the LogicMonitor report.  This column contains the account site name
which is then trimmed via the columnStrip function.

The user is also asked to select the column of values they wish to filter their list of accounts by.

A dictionary is created consisting of trimmed account sites as keys and indicated values as values (reduntant I know...)

The user is asked to specify how they would like to filter this dictionary (by specifying a comparison operator and value).

The program performs a VLOOKUP where, for every contact in the SF report, if it exists in the dictionary, the value is
appended in a column with a user specified header.  Contacts from accounts not in the dictionary are removed from the
SF report.

The new .csv file is saved under a user specified filename when the program is run.
