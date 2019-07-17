'''
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''


def gen_seven(r):
    i = 0
    while i < r:
        ri = i
        i = i + 1
        if ri % 7 == 0:
            yield ri

for num in gen_seven(100):
    print(num)