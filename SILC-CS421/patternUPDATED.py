

# All your code should be between BEGIN and END.
# Do not change the rest of the program
# Please visit this video first
# http://www.viewpure.com/riL_xn6BKD8?start=0&end=0
# You can use pythontutor OR python IDLE to develop the program
# But once the program is working, please use Python IDLE
# to save the file to "pattern.py"
# and submit that file to google classroom

def pattern(input_char="*", line_count=5, display_mode="RIGHT"):
    #BEGIN your code

    display = display_mode
    #Generating the correct number of spaces for display_mode
    mode = ""

    if display == "CENTER":
        mode = " "
    elif display == "RIGHT":
        mode = "  "


#Converting to integer
line_int = int(line_count)

#Finding length to ensure program works with multiple character patterns
length = len(input_char)
for x in range(line_int):
    print(space * (line_int-x+1)*length + input_char * (2*x+1)

          #END your code



          # Assignment 10  test cases

          #Test Case 1
          print('Test Case 1:  pattern("*",5,"RIGHT")')
          pattern("*", 5, "RIGHT")

          #Test Case 2
          print('Test Case 2:  pattern("@",6,"LEFT")')
          pattern("@", 6, "LEFT")

          #Test Case 3
          print('Test Case 3:  pattern("#",10,"CENTER")')
          pattern("#", 10, "CENTER")

          #Test Case 4 with all defaults
          print('Test Case 4: pattern()')
          pattern()

          #Test Case 5 pass in only two params and third is a default
          print('Test Case 4: pattern("X", 5)')
          pattern("X", 5)

          #Test Case 6: Take the inputs from the user on all three
          # and use those to test your method
          a=input("Enter your character? ")
          b=input("How many lines do you need? ")
          c=input("How do you want to justify the display (LEFT, RIGHT, CENTER)? ")
          pattern(a, b, c)
