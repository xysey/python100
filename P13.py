'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
sentence = input()
letters, digits = 0, 0
for char in sentence:
    if char.isalpha():
        letters = letters + 1
    elif char.isdigit():
        digits = digits + 1

print(f"LETTERS {letters}\nDIGITS {digits}")