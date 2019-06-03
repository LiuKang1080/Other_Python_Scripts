from datetime import datetime


def factorial(number):
    n = 1
    count = int(number)
    while count > 0:
        n *= count
        count -= 1
    print(n)


factorial(10)

t1 = datetime.now()
factorial(500)
t2 = datetime.now()
print(t2 - t1)
