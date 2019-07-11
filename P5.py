'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class ForTheString():
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

if __name__ == "__main__":
    myString = ForTheString()
    myString.getString()
    myString.printString()