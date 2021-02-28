import random

x = int(input('Fibonacci Number:'))


def Fib(x):
    if x < 0:
        print('Incorrect input')
    elif x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return Fib(x - 1) + Fib(x - 2)

c = Fib(x)

print('Number Received:', c)
w = 0
if x == 0 or x == 1 or x == 2 or x == 3:
    print(c, 'Is not a prime Number')
else:
    for i in range(0, 20):

        a = random.randint(1, c - 1)

        if (a ** (c - 1) - 1) % c == 0:
            w += 1
    if w == 20:
        print(c, 'Prime Number')
    else:
        print(c, 'Is not a prime Number')
