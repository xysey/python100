'''
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma - separated numbers.
Suppose the following input is supplied to the program:
1, 2, 3, 4, 5, 6, 7, 8, 9
Then, the output should be:
1, 3, 5, 7, 9 <--- I think the output shoul be the squares of each odd number...

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
numbers = input().split(', ')
odd_num_sq = [str(int(num)**2) for num in numbers if int(num) % 2 != 0]
print(", ".join(odd_num_sq1,))