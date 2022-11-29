# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: This script will request a quantity of numbers to cube, gather the numbers to cube, cube those numbers,
#              save the numbers to a binary file, then read the binary file and return the data to the user.
# ChangeLog (Who,When,What):
# Jason Verberne,11/27/2022,Created script for Assignment07
# Jason Verberne,11/28/2022,Added notes
# ---------------------------------------------------------------------------- #

import pickle # Needed for saving via the 'pickle' method


# Data ---------------------------------------------------------------------- #
intChoice = "Pending" #not an integer initially so the code will loop until correct data is provided by the user
strFile = "NumberCube.dat"
count_1 = 1
lstNumbers = []
dicNumCube = {}


# Processing  --------------------------------------------------------------- #
def verify_integer (user_choice):
    '''Verifies input from user is type Integer with possible exceptions

    :param user_choice: try verifies user entered an integer, except ValueError if not an integer
    :return: (integer) returns user input if integer or "Pending" if not integer to continue the loop
    '''
    try:
        choice = int(user_choice)
        return choice
    except ValueError as e:
        print("\nError: You must choose an integer. Please try again.\n")
        print("=" * 15 + "Technical Data Info"+"=" * 15)
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
        print("=" * 49)
        print()
        return "Pending"
    except Exception as e:
        print("There was a non-specific error!")
        print("=" * 15 + "Technical Data Info"+"=" * 15)
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
        print("=" * 49)
        print()
        return "Pending"

def verify_float(user_input):
    '''Verifies input from user is type float with possible exceptions

    :param user_input: Function verifies user_input is type float.
    :return: (float) returns user input if it was initially float or 0 (zero) if not float
    '''
    try:
        choice = float(user_input)
        return choice
    except ValueError as e:
        print("\nError: You must choose a float to cube. A 0 (zero) will be entered for this calculation.\n")
        print("=" * 15 + "Technical Data Info"+"=" * 15)
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
        print("=" * 49)
        print()
        return int(0)
    except Exception as e:
        print("There was a non-specific error!")
        print("=" * 15 + "Technical Data Info"+"=" * 15)
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
        print("=" * 49)
        print()
        return int(0)

def save_data(data,file_name):
    ''' Saves the list of numbers from the user to the dat file.

    :param data: (list): saves the lstNumbers from user and their cubes to the pickle file
    :param file_name: (file): is the file name to which the information is being saved
    :return: n/a
    '''
    file = open(file_name,"wb")
    pickle.dump(lstNumbers,file)
    file.close()
    return()

def read_data(file_name):
    ''' Opens the saved pickle file, loads data, stores data in variable file_info, and uses for loop to
        print stored data

    :param file_name: (file): is the file name from which the information is being retrieved
    :return: n/a
    '''
    file = open(file_name,"rb")
    file_info = pickle.load(file)
    file.close()
    for row in file_info:
        print("The cube of " + str(row["Number"]) + " equals: " + str(row["Cube"]))
    return()


# Presentation (Input/Output)  -------------------------------------------- #
print("This program will cube numbers you provide, save the data, and return the information.\n") #header info only

while intChoice == "Pending": #loops until a valid integer is provided by the user
    intChoice = verify_integer(user_choice=input("Please enter the quantity of numbers you wish to cube: "))
print("""==============================""")

while count_1 <= int(intChoice): #loops until count exceeds user quanitity. Verifies user input is a float.
    fltUser_Number = verify_float(user_input=input("What number would you like to cube? "+ str(count_1) + ": "))
    dicNumCube = {"Number":fltUser_Number,"Cube":round(fltUser_Number**3,2)}
    lstNumbers.append(dicNumCube)
    count_1 += 1

print("""
Your data was saved to a file.
==============================""")

save_data(data=lstNumbers,file_name=strFile) #calls the function to pickle the data

read_data(file_name=strFile) #calls the function to read saved data, save to variable file_info, and print data entered.

print("""==============================""")

input("\n*** You are now leaving the program*** \n\tHit 'Enter' to exit.") #pauses the program before exiting
