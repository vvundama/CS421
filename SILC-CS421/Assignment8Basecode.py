#Assignment 8: Implement isPalindrome and isAnagram methods
#Assignment 8: Test for both positive and negative cases


# Panlindrome:  See  https://en.wikipedia.org/wiki/Palindrome#Characters,_words,_or_lines
# This function returns "TRUE" if the given word is a palindrome
#           else it returns "FALSE"
palindromeInput = input("Type in a word here")
palindromeListORI = list(palindromeInput)
palindromeListREV = list(palindromeInput)
palindromeListREV.reverse()

strORI = ''.join(str(x) for x in palindromeListORI)
strREV = ''.join(str(x) for x in palindromeListREV)

def isPalindrome(strORI, strREV):
    if strORI == strREV:
        return "TRUE"
    else :
        return "FALSE"


# Anagram:  See  https://en.wikipedia.org/wiki/Anagram
# This function returns "TRUE" if the two words are Anagrams
#           else it returns "FALSE"
def areAnagrams(word_1, word_2):
    if(sorted(word_1) == sorted(word_1)):
        return "TRUE"
    else :
        return "FALSE"


#  Test cases for the two functions
# Palindrome positive test cases (should return TRUE)
# radar, level, rotor, kayak, racecar, madam
x = isPalindrome("radar")
print("is radar palindrome? = ",  x)

# Palindrome positive test cases (should return FALSE)
# python, java, silc
x = isPalindrome("python")
print("is python palindrome? = ",  x)


# Anagram positive test cases (should return TRUE)
# evil=vile,  silent=listen,  eleven plus two=twelve plus one
word_x = "evil"
word_y = "vile"
result = areAnagrams(word_x, word_y)
print("Are ", word_x, " and ", word_y, " anagrams? = ", result)


# Anagram positive test cases (should return FALSE)
# python = pxthon, java = lava, a = abcdefghijklmnopqrstuvwxyz
word_x = "python"
word_y = "pxthon"
result = areAnagrams(word_x, word_y)
print("Are ", word_x, " and ", word_y, " anagrams? = ", result)
