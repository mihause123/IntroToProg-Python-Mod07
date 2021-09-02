# ------------------------------------------------- #
# Title: Assignment07
# Description: A try-catch with manually raised errors
# ChangeLog: (Who, When, What)
# Michael Hause,8/24/2021,Created Script
# Michael Hause,9/02/2021,edited script
# ------------------------------------------------- #
import pickle
filename = 'NameAge.txt'
strName = ''
intAge = ''
dicrow = {}
lstTable = []



print("Please enter a Person's name and their age")
strName = str(input("Name: "))  # input for the name

while True:   #while loop that loops until a valid integer is entered by the user
    try:
        intAge = int(input("Age: "))  # input for the age as integer for purpose of error handling
        break
    except ValueError:   # prints response when a non integer is entered by the user
        print("please enter a valid number")

dicRow = {"Name": strName, "Age": intAge}  # adds those inputs to a dictionary row
lstTable.append(dicRow)  # appends rows to the table

outfile = open(filename, 'wb')  #open file in binary write mode
pickle.dump(lstTable, outfile)  #dumps pickled data into text file
print(lstTable)

infile = open(filename, 'rb')  #opens file in binary read mode
try:
    while (True):
        NewlstTable = pickle.load(infile) # unpickles file and loads contents
        print(NewlstTable) # opens new table to compare
except EOFError:
    pass
infile.close()
