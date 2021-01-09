#----------Start Palindrome Function----------#

#Asking user to input value
palindromeInput = input("Type in a word here")
#Converting input to a list
palindromeListORI = list(palindromeInput)

#Making another list from user input
palindromeListREV = list(palindromeInput)
#Reversing the second input list 
palindromeListREV.reverse()

#Converting both lists into strings
strORI = ''.join(str(x) for x in palindromeListORI)
strREV = ''.join(str(x) for x in palindromeListREV)

#Printing both strings containing the lists
print("Your word: " + strORI)
print("Your word reversed: " + strREV)

#Checking wether original list and reversed lists are the same
if strORI == strREV:
    #If the lists are the same they are a palindrome
    print("The word, " + strORI + ", is a palindrome.")
else :
    #If not, the word is not a palindrome
    print("The word, " + strORI + ", is not a palindrome.")

#-----------End Palindrome Function-----------#


#----------Start Anagram Function----------#

#Asking user to input two words 
anagramInput1 = input("Type in a word here")
anagramInput2 = input("Type in another word here")

#Defining function
def areAnagrams(word_1, word_2):
    #Using the sorted function to sort the inputs 
    #If words are anaagrams, sorted inputs will be the same
    if(sorted(word_1) == sorted(word_1)):
        print("Word One: " + word_1)
        print("Word Two: " + word_2)
        print("The two words you entered are anagrams.")
    #Otherwise the inputs aren't palindromes
    else :
        print("Word One: " + word_1)
        print("Word Two: " + word_2)
        print("The two words you entered are not anagrams.")

#Setting inputs equal to "word_1" and "word_2"
word_1 = anagramInput1
word_2 = anagramInput2
#Running "word_1" and "word_2" in function
areAnagrams(word_1, word_2)

#----------End Anagram Function----------#