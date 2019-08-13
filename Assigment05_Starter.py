#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   Daveoverman
# Date:  August 12, 2019
# ChangeLog: (Who, When, What)
# David Overman, 8/12/2019, Added code to try assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

objFileName = "Todo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

objData = open(objFileName, "r+")
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
        objData = open(objFileName, "r+")
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
