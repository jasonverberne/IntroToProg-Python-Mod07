Jason Verberne  
November 28, 2022  
Foundations of Programming: Python  
Assignment07  
https://github.com/jasonverberne/IntroToProg-Python-Mod07 (external link)

**_PICKLE AND ERROR HANDLING_**

**INTRODUCTION**  

This paper will discuss the steps taken in completing Assignment07 of the Foundations of Programming: Python Course. This assignment required the creation of a script that would demonstrate the Python Pickle feature and Exception Handling. 

**BACKGROUND**

Prior projects and knowledge that contributed to the successful completion of this assignment include: 
1.	Assignment01: This assignment requested the creation of a Python script that would accept the first and last name of a user and, in return, would display the concatenated information provided as the full name.  
2.	Assignment02: This assignment requested the creation of a Python script that would independently request two numbers from the user and, in return, would display the sum, difference, product, and quotient of those two numbers. 
3.	Assignment03: This assignment requested the creation of a Python script that would gather a household item from the user, gather an estimated value of the item, and save that information in text file.  
4.	Assignment04: This assignment requested the creation of a Python script that would allow the user to select from a menu to 1) gather multiple household items and estimated costs, 2) display the information gathered from the user back to the user, and save that information in text file and exit the program.
5.	Assignment05: This assignment required the modification of a Python script that would allow the user to select from a menu to show task and priority data, add a new task and priority to the list, remove an existing dictionary from the list, save the information to a text file, and exit the program.
6.	Assignment06: This assignment required modification of / addition to a Python script that would allow the user to select from a menu to show task and priority data, add a new task and priority to the list, remove an existing dictionary from the list, save the information to a text file, and exit the program.
7.	Independent study prior to the course, including:  
  a.	YouTube: https://www.youtube.com/watch?v=rfscVS0vtbw, freeCodeCamp.org, Mike Dane (presenting), uploaded July 11, 2018 (External Site)  
  b.	Pierce County Library Book: Begin to Code with Python, Miles, Robert S., Microsoft/Pearson Education, Inc., 2018, ISBN 9781509304523
I chose to perform my coding in PyCharm instead of using IDLE. 

**DOCUMENT FOCUS**  

Assignment 07 had different elements, including:  
1.	Researching the Pickle Method and Exception Handling in Python.
2.	Creation of a script that demonstrates the Pickle Method and Exception Handling in Python.

**_RESEARCH_**

1.	Exception Handling 
    -	https://www.geeksforgeeks.org/python-exception-handling (external link), October 11, 2022, contributions by Akanksha_Rai, nikhilaggarwal3, anuragsharma011011, punamsingh628700, swarajjalkote98  
      * I like the geeksforgeeks.com site because the information is often up to date.  
      * This page provides examples of code that can be studied and copied/pasted in Python for review.  
      * For me, this page follows a logical, step by step approach to reviewing Exception Handling in Python, including covering syntax error vs exceptions, try/except statements and catching errors, and try/else/finally statements.
b.	https://practicaldatascience.co.uk/data-science/how-to-try-except-for-python-exception-handling (external link), Matt Clarke, December 24, 2021
i.	This article does a good job of explaining the try/except/finally method while using opening a file as an example. 
ii.	The explanation followed a linear progression but was still geared towards a new user.
2.	Pickle Function
a.	https://www.datacamp.com/tutorial/pickle-python-tutorial (external link),  Theo Vanderheyden, Apr 2018, Theo Vanderheyden
i.	The first half of this article does a good job of explaining the ‘what and when’ of Pickling, and even discusses a basic comparison and contrast against JSON, which is useful for a new user. 
ii.	The second half, while I didn’t fully understand the examples, began to demonstrate the limitations of the Pickle Method, specifically if you try to pickle Lamda functions. As a result, I’ll be reading more into these other areas soon to learn more. 
b.	https://www.youtube.com/watch?v=Pl4Hp8qwwes (external link), Mark Jay, November 12, 2017
i.	This YouTube video provided a different approach to the Pickle Method than that generally show in class, specifically by using the ‘with’ method. Many of the concepts were the same. I find this information useful so if I see this in the future, I will be more aware and familiar with this approach.
ii.	 The presenter followed a logical approach in explaining the information. 

-- PYTHON SCRIPT – DEMONSTRATE PICKLE AND EXCEPTION HANDLING –

HEADER
Before writing code that will actually perform the task, it is important to provide supporting information to any programmer, including myself for later use, about the purpose and historical activities of the code. This information does not have to be lengthy, although it could be if needed. In this case, I provided a description of what the code would do, then provided the Who, What, and When of the changes. 
-----------------------------------------------------------------------------------
 
-----------------------------------------------------------------------------------
Figure 1: Header of Python code

Because this information is not intended to be processed by Python, I started each line with a “#” symbol. In Python, any line that begins with a number sign (aka the pound sign) will not be processed by Python. Alternatively, I could have used two sets of three single quotes (‘’’) with the header information between the sets, which would have provided the same result. 

CODE INFORMATION 
The notable elements of this code include:
1.	variables - the variables I used to store the data are:
a.	intChoice – used to store the user’s information from the input() function
b.	strFile – stores the name of the dat file for storing pickled data
c.	count_1 – stores numbers for counting in a loop
d.	lstNumbers - represents a list of dictionaries
e.	dicNumCube - holds the dictionary which is appended to lstNumbers. The dictionary contains user specified numbers and the cube (^3) of those numbers
2.	User defined functions – used to process information/data
a.	verify_integer – uses try/except to verify input from the user is an integer
b.	verify_float – uses try/except to verify input from the user is a float
c.	save_data – saves a list of dictionaries that contain the user chosen number and the cube of that number
d.	read_data – opens the saved pickle file, loads data, stores data in variable file_info, and uses for loop to print stored data
3.	.append – this method appends the identified object to the list
4.	Try/except – this method first attempts to run code under the ‘try’ but if an error occurs, the except runs, assuming no specific error has been identified, such as ValueError, or the specific error matches the one that occurred
5.	for/in – this loop iterates through an object, in this case a list, and performs the programmer defined action on each object in the list.
6.	Pickle open/close file and dump/load data – this includes opening/closing files and reads/writes to/from the file allowing potential updates to occur or the program to read from the opened file. In this case, it was a dat file. 
7.	input() - this function allows the user to provide information to be stored in Python
8.	return – used as the end of a function, this statement defines what is returned after the function is complete 
-----------------------------------------------------------------------------------
SEPARATION OF CONCERN
 “Separation of Concern,” is defined as, “In computer science, separation of concerns (SoC) is a design principle for separating a computer program into distinct sections, so that each section addresses a separate concern. A concern is a set of information that affects the code of a computer program.” https://en.wikipedia.org/wiki/Separation_of_concerns (external link), 2019. In our Assignment06 template, we had several notes identifying the separate areas. 
 
 
 
-----------------------------------------------------------------------------------
Figure 2, Separations of Concern from the provided script
 
 
 
-----------------------------------------------------------------------------------
Figure3:  Python script for Assignment 07

CODE DETAILS
1.	Line 10: The keyword import is used to make Pickle available in the script
2.	Lines 14-18: Data/variables that are used in the script (defined under ‘Code Information’ above)
3.	Lines 22-46: This function uses the try/except method to evaluate if the user provided information (via the input() function) is a type integer. Line 29 sets the local variable ‘choice’ to an integer (user_choice). If an error occurs because user_choice is not an integer, then the except ValueError is processed. The user is provided with ‘layman’ guidance and ‘technical’ guidance. A return of string ‘Pending’ will cause the while loop to continue until the user enters an integer. Although I could not think of or cause any other error, I included “except Exception” as a catch-all. 
4.	Lines 48-72: This function uses the try/except method to evaluate if the user provided information (via the input() function) is a type float. This function works similar to the verify_integer function (Lines 22-46). However, instead of returning string ‘Pending’ to continue the loop, I chose to demonstrate a different option of forcing a default zero (0) as the number to cube for the user if they do not provide a float number.
5.	Lines 74-84: This function uses the pickle method to open the file_name in write mode (“wb”). Then the lstNumbers list is saved to the file, in this case "NumberCube.dat."
6.	Lines 86-98: This function uses the pickle method to read/load the data from the file_name (NumberCube.dat). Local variable file_info is used to store the data from the opened file, then the file is closed. File_info is then used in a for/in loop to extract the ‘Number’ and ‘Cube’ from the list of dictionaries and print them to the user in an understandable format. 
7.	Line 102: This is the first line of code when the program begins that causes some action other than the computer just loading the code. This message is provided to the user so they understand the intent of the program. 
8.	Line 104-105: This while loop gathers the user input on the quantity of numbers the user wants the program to cube. The while loop will continue as long as the intChoice variable is equal to ‘Pending.’ The verify_integer function is called to verify the user provides an integer as a response. If not, the function returns ‘Pending’ to continue the loop.
9.	Line106: This line provides the user an aesthetic separation between information.
10.	Lines 108-112: This while loop gathers the user input on the numbers they want the program to cube and store in a file. Line 109 calls the verify_float function to verify the user input is a float number. This while loop will only loop as many times as the user previously indicated in the prior while loop by iterating the count_1 variable. After verifying the user entered a type float or the except returning a zero, Line 110 inserts the information and calculated cube (^3) into a dictionary, which line 111 then appends to the list lstNumbers.
11.	Lines 114-116: Same as line 106
12.	Line 118: This line calls the save_data function (to save the data to a dat file via the Pickle method)
13.	Line 120: This line calls the file_name function (to read & print the previously saved data from the dat file)
14.	Line 122: Same as line 106
15.	Line 124: This line provides a pause in the program and notifies the user they are exiting the program
RESULTS
The results of the program were as expected, with the program 1) gathering the quantity of numbers the user wanted to have the program cube (^3), 2) using try/except to validate the data types were appropriate, 3) having the user enter the float numbers to cube, 4) saving the data via the Pickle method, and 5) reading and returning the data to the user from the previously saved file.  Note the example below intentionally contains error in user input to demonstrate the error handling capability of the script. 
-----------------------------------------------------------------------------------
```C:\_PythonClass\Assignment07>python Assignment07.py
This program will cube numbers you provide, save the data, and return the information.

Please enter the quantity of numbers you wish to cube: ABC

Error: You must choose an integer. Please try again.

===============Technical Data Info===============
Built-In Python error info:
invalid literal for int() with base 10: 'ABC'
Inappropriate argument value (of correct type).
<class 'ValueError'>
=================================================

Please enter the quantity of numbers you wish to cube: 3
==============================
What number would you like to cube? 1: 4.3
What number would you like to cube? 2: XYZ

Error: You must choose a float to cube. A 0 (zero) will be entered for this calculation.

===============Technical Data Info===============
Built-In Python error info:
could not convert string to float: 'XYZ'
Inappropriate argument value (of correct type).
<class 'ValueError'>
=================================================

What number would you like to cube? 3: 6

Your data was saved to a file.
==============================
The cube of 4.3 equals: 79.51
The cube of 0 equals: 0
The cube of 6.0 equals: 216.0
==============================

*** You are now leaving the program***
        Hit 'Enter' to exit. ```
-----------------------------------------------------------------------------------
Figure 4:  Results after running the Python code and user providing input.

 
-----------------------------------------------------------------------------------
Figure 5:  Saved Text File of the User Input

CHALLENGES AND LEARNING 
There were a few challenges and points of learning from this week’s assignment. 
•	The greatest coding challenge was the creation of the loop after the try/except found an exception. I resolved this by using ‘return “Pending”’ to continue the loop.
•	I also appreciate the additional effort in proper documentation, and the need to be clear and concise.
•	This lesson greatly helped my understanding of Pickling, which is something I studies a few months ago, but did not fully understand.

SUMMARY
This document described the steps taken and approach to completing Assignment07 of the Foundations of Programming: Python Course. It discussed the prior knowledge and background information considered when writing this script, the major sections of the script, and the returned results the user would expect. 
