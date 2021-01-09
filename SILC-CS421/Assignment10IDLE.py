Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Assignment 10
# All your code should be between BEGIN and END. 
# Do not change the rest of the program
# Please visit this video first
# http://www.viewpure.com/riL_xn6BKD8?start=0&end=0 
# You can use pythontutor OR python IDLE to develop the program
# But once the program is working, please use Python IDLE
# to save the file to "pattern.py" 
# and submit that file to google classroom


def pattern(input_char = "*", line_count = 5, display_mode = "RIGHT"):

    for x in range(b):
        print(c*(b-x-1)+a*(2*x+1))
    else:
        print('  '*(5-x-1)+'*'*(2*x+1))

    
    

# Assignment 10  test cases

#Test Case 1
print('Test Case 1:  pattern("*",5,"RIGHT")')
pattern("*",5,"RIGHT")

#Test Case 2
print('Test Case 2:  pattern("@",6,"LEFT")')
pattern("@",6,"LEFT")

#Test Case 3
print('Test Case 3:  pattern("#",10,"CENTER")')
pattern("#",10,"CENTER")

#Test Case 4 with all defaults
print('Test Case 4: pattern()')
pattern( )

#Test Case 5 pass in only two params and third is a default
print('Test Case 4: pattern("X", 5)')
pattern("X",5)

#Test Case 6: Take the inputs from the user on all three 
# and use those to test your method
a = str(input("Enter your character? ") or "*")

b = int(input("How many lines do you need? ") or "5")

c = str(input("How do you want to justify the display (LEFT, RIGHT, CENTER)? ") or "RIGHT")
if c == "LEFT":
    c = ''
elif c == "CENTER":
    c = ' '
elif c == "RIGHT":
    c = '  '

pattern(a,b,c)


