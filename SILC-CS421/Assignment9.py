# Assignment 9 (Exploring Tuples of tuples)

def getAverageAge(big_tuple):

    total_age = 0
    for x in big_tuple:
        name, age, marks = x
        total_age = total_age + age

    no_of_students = len(big_tuple)

    average_age = total_age / no_of_students

    return average_age


def getAverageMarks(big_tuple):

    total_marks = 0
    for x in big_tuple:
        name, age, marks = x
        total_marks = total_marks + marks

    no_of_students = len(big_tuple)

    average_marks = total_marks / no_of_students

    return average_marks

#----------Here is an alternative method that is applicable in Python 3----------#

#def getLowestMark(big_tuple):
    
    #MARKtupleLOW = zip(*big_tuple)[2]
    #LowestMark = min(MARKtupleLOW)

    #return LowestMark
    

#def getHighestMark(big_tuple):
    
    #MARKtupleHIGH = zip(*big_tuple)[2]
    #HighestMark = min(MARKtupleHIGH)

    #return HighestMark

#----------End alternate method----------#

def getLowestMark(big_tuple):
    
    LowestSCORE = []

    for x in big_tuple:
        LowestSCORE.append(x[2])
        LowestMark = min(LowestSCORE)

    return LowestMark
    

def getHighestMark(big_tuple):
    
    HighestSCORE = []

    for x in big_tuple:
        HighestSCORE.append(x[2])
        HighestMark = max(HighestSCORE)

    return HighestMark
    

    #getSummary(big_tuple)
    #This method returns a “tuple” reflecting these values
    #  total_no_of_students
    #  average_age
    #  average_marks
    #  highest_mark
    #  lowest_mark
    # ensure that this method calls other mini-methods
def getSummary(big_tuple):
    #BEGIN your code
    #1. total_no_of_students
    total_no_of_students = len(big_tuple)

    #2. average_age
    average_age = getAverageAge(big_tuple)

    #3. average_marks
    average_marks = getAverageMarks(big_tuple)

    #4 highest_mark
    highest_mark = getHighestMark(big_tuple)

    #5 lowest_mark
    lowest_mark = getLowestMark(big_tuple)

    # construct the summary tuple
    summary_tuple = (total_no_of_students, average_age,
                     average_marks, highest_mark, lowest_mark)

    return summary_tuple
    #END your code


#========== Test Data ===========
# create student tuples
student_1 = ("abe", 16, 88)
student_2 = ("barb", 30, 72)
student_3 = ("chris", 14, 92)
student_4 = ("dan", 20, 80)
student_5 = ("ethan", 16, 60)

#create a bigger tuple representing the class
php_class = (student_1, student_2, student_3, student_4, student_5)

# just for testing the mini-method
print("average age ", getAverageAge(php_class))

# call the above method
summary_tuple = getSummary(php_class)
total_no_of_students, average_age, average_marks, highest_mark, lowest_mark = summary_tuple

print("total no of students = ", total_no_of_students)
print("average age = ", average_age)
print("average marks = ", average_marks)
print("highest marks = ", highest_mark)
print("lowest makrs = ", lowest_mark)
