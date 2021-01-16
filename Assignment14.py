#----Assignment 14 Exploring Classes and Objects----#

#Defining class for Paper
class Paper:

    #Properties of class
    def __init__(self, company, length, width):
        self.company = company
        self.length = length
        self.width = width

    #Function makes sure that each instance is differentiated from the others
    def getDetails(self):
        print("Company : " + self.company)
        print("Length : " + self.length)
        print("Width : " + self.width)

#Instance number one
paper_georgiaPacific = Paper("Georgia Pacific" , "10 in" , "8 in")
paper_georgiaPacific.getDetails()

#Instance number two
paper_domtar = Paper("Domtar" , "11 in" , "9.5 in")
paper_domtar.getDetails()
