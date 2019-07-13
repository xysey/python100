'''
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
��
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
net = 0
while True:
    i = input().split(' ')
    if i[0] == 'D':
        net = net + int(i[1])
    elif i[0] == 'W':
        net = net - int(i[1])
    else:
        break
print(net)
