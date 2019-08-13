#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   <YOUR NAME HERE>, ???, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

objFileName = "Todo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

objData = open(objFileName, "r")
for line in objData:
    (val1,val2) = line.split(",")
    dicRow [str("Task")] = val1
    dicRow [str("Priority")] = val2

 # Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        objData = open(objFileName, "r")
        for line in objData:
            (key, val) = line.split(",")
            dicRow[str(key)] = val
        print("The  following Data is saved:\r", dicRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while(True):
            taskID = str(input("What's your task?:\n"))
            taskPri = str(input("What's your task priority? (high, med, low):\n"))
            dicNewRow = {"Task": taskID, "Priority": taskPri}
            lstTable.append(dicNewRow)
            strSaveToFile = input("Are you done entering? (y/n):")
            if (strSaveToFile.lower()) == 'y':
                print("The  following Data was saved:\n\r", lstTable)
            break

    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        strSaveToFile = input("Are you ready to save? (y/n):")
        if (strSaveToFile.lower()) == 'y':
            objF = open(objFileName, "a")
            objF.write(str(dicRow))
            objF.close()
            print("The  following Data was saved:\n\r", lstTable)
        continue
    elif (strChoice == '5'):
        break #and Exit the program