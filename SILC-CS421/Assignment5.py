#************************** CS421: Assignment 5 **************
#
#  There are four sections in this assignment. Each section is worth 5 points.
#  Sections 1 and 2 count towards Assignment 5.
# Sections 3 and 4 count towards Assignment 6.
#  Skeleton code is already given. 
#  You only need to add your code between BEGIN and END lines in each section.
#
# Do NOT hardcode the output; You need to write python code so that it works whether
# you have 10 students in the list OR 1000 students in the list.
#
#  Use pythontutor.com to implement each section.
#  Save the complete implementation to a file called "a5_lists.py" and submit the file to Google Classroom
#
# How to save the code from PythonTutor to a file?
#           Select the entire code (Ctrl + A)
#           Copy the entire code (Ctrl + C)
#           Open notepad or any other editor you use to write text files.
#           Paste the entire code (Ctrl + V)
#           Save the code to a file (Ctrl +S)
# ************************************************************


#----------------------------------------------------------------------------
# A.5.1 --> Assume that some students registered twice for the same class.
# You need to write a program to remove the duplicate registrations from a list
#----------------------------------------------------------------------------

# Creating the list with duplicate values
students = ["abe", "barb", "chris", "abe", "dan", "chris", "ellie", "peter"]
print("All students --> ", students)

# Creating two empty lists
student_temp = []
unique_students = []
for x in students:
    # Essentially this "if" statement is populating the student_temp list  
    if x not in student_temp:
        student_temp.append(x)
    # If the "if" statement runs across a duplicate value it will get printed in this seperate list
    else:
        unique_students.append(x)

# Printing out both lists
print("Students who registered once: --> ", student_temp)
print("Students who registered twice: --> ", unique_students)

#----------------------------------------------------------------------------
#A.5.2 --> Assume that some students registered both html and python classes
# Find out the list of students who registered for both the classes.
#----------------------------------------------------------------------------

# Creating two lists of students
html = [ "barb", "dan", "ellie", "abe", "chris"]    
python = ["henry", "chris", "dan", "ellie", "frank", "gavin"] 

# Using the "set" fuction for both lists and storing result in variable "dupe"
dupe = set(html) & set(python)

# Printing html and python list, plus the dupe variable which contains the duplicate names
print("html students --> ", html)
print("python students --> ", python)
print("duplicates --> ", dupe)