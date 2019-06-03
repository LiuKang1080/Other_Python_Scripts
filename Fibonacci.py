def fibonacci():
    a, b = 0, 1
    while b < 100:
        a, b = b, a + b
        print(a)


fibonacci()

# ======================


def fibonacci2():
    a, b = 0, 1
    while b < 100:
        yield a
        a, b = b, a + b


fib_gen = fibonacci2()
print(fib_gen)

for i in fib_gen:
    print(i)


