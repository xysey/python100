'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
upper_case, lower_case = 0 , 0
sentence = input()
for char in sentence:
    if char.isupper():
        upper_case = upper_case + 1
    elif char.islower():
        lower_case = lower_case + 1
print(f"UPPER CASE {upper_case}\nLOWER CASE {lower_case}")