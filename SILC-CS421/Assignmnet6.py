#************************** CS421: Assignment 6 **************
#
#  There are four sections in this assignment. Each section is worth 5 points.
                                                                            #  Sections 1 (5.1) and 2 (5.2) count towards Assignment 5.
#  Sections 3 (6.1) and 4 (6.2) count towards Assignment 6.
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
#A.6.1 --> Assume that html class is overcrowded with too many registrations.
# Since that class is too big, SILC decided to split the HTML class
# into two sections html_a and html_b
# All the students whose name starts with (a, b....,l, m) will be in html_1
# And all the students whose name starts with (n,o,...., y,z) will be in html_2
# 
# You are given a big list called "html"
# Write python code to create two new lists "html_a" and "html_b" per the above logic.
# Finally, print all three lists in alphabetical order
#----------------------------------------------------------------------------

html = [ "guy", 
"madeline", 
"parker", 
"chris",
"tom", 
"ursula", 
"ramesh", 
"lisa", 
"staci", 
"jordan", 
"emmett", 
"vinny", 
"brian", 
"zora", 
"oliver", 
"polly", 
"kingston", 
"olivia", 
"xavier", 
"fiona", 
"zack", 
"harmony", 
"barb", 
"samson", 
"ariel", 
"emma", 
"yasmine", 
"crystal", 
"dan", 
"xenia", 
"irving", 
"tiffany", 
"noah", 
"umesh", 
"yates", 
"victoria", 
"desiree", 
"quinn", 
"wendy", 
"frank", 
"henry", 
"mike", 
"isabella", 
"nora", 
"julie", 
"lincoln", 
"alex", 
"kim", 
"raven", 
"watson", 
"ganga"
]    
html_a = [] 
html_b = []

#Converting all the name to uppercase so no confusion happens
html = [each_string.upper() for each_string in html]

#Sorting list in alphabetical order
html.sort()

#For all letter before "N" add them them to html_a
for x in html:
    if x[0] < "N":
        html_a.append(x)
    #All other names are added to html_b
    else:
        html_b.append(x)

#Printing out all of the lists
print("html --> ", html)
print("html_a --> ", html_a)
print("html_b --> ", html_b)

#----------------------------------------------------------------------------
# A.6.2 --> Assume that python class has 10 students.
# Instructor is keeping track of their attendance on every saturday.
# by keeping the list of students present in another list.
# So, You are given an original list of 10 students.
# And for each saturday, another smaller list is given to you.
# You will write a program to provide attendance chart as follows
#
#    s1    A    P   P   P
#    s2    P    P   P   A
#    ....................
#    s10   A    A   A   A
#----------------------------------------------------------------------------

# define students list
python = ["abe", "barb", "chris", "dan", "ellie", "gabby", "henry", "isabelle", "jack", "larry"]

# define the attendance list
week_1  = ["barb", "chris", "dan", "ellie", "henry", "isabelle", "jack"]
week_2  = ["abe", "barb", "chris",  "ellie", "gabby", "henry", "isabelle",  "larry"]
week_3  = ["abe", "barb",  "henry", "isabelle", "jack", "larry"]
week_4  = ["abe", "barb", "chris", "dan", "ellie", "gabby", "henry", "isabelle", "jack"]

# defint the list to hold the attendance
attendance_report = [ ]

#If student name from python appears in week_1 it marks "P", if student name from python not in week_1 it marks "A"
for x in python:
    student_attendence1 = [x]
    if x in week_1:
        student_attendence1.append(x)
        print("P")
    else:
        print("A")

#If student name from python appears in week_2 it marks "P", if student name from python not in week_2 it marks "A"
for x in python:
    student_attendence2 = [x]
    if x in week_2:
        student_attendence2.append(x)
        print("P")
    else:
        print("A")

#If student name from python appears in week_3 it marks "P", if student name from python not in week_3 it marks "A"
for x in python:
    student_attendence3 = [x]
    if x in week_3:
        student_attendence3.append(x)
        print("P")
    else:
        print("A")

#If student name from python appears in week_4 it marks "P", if student name from python not in week_4 it marks "A"
for x in python:
    student_attendence4 = [x]
    if x in week_4:
        student_attendence4.append(x)
        print("P")
    else:
        print("A")

    #Combining lists containing "A" and "P" to form student_attendence
    student_attendence = student_attendence1 + student_attendence2 + student_attendence3 + student_attendence4
    #Adding student_attendence to attendance_report
    attendance_report.extend(student_attendence)
    #Adding attendance_report to attendence_list
    attendance_list = [attendance_report]

# print students attendance report. Unpack the list so that we get each element on a new line
for x in attendance_report:
    print(*x)
