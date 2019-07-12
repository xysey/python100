'''
Question 9
Level 2

Question��
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
lines = []
while True:
    string = input()
    if string:
        lines.append(string.upper())
    else:
        break

for line in lines:
    print(line)