# For each number of iterations double the amount provided


def double_compound(amount, iterations):
    print("Initial value: " + str(amount))

    for i in range(0, iterations):
        amount *= 2

    print("Value after being doubled at each iteration: " + str(amount))
    print("\n")


# 1,000$ doubled 10 times is = 1,024,000
double_compound(1000, 10)
double_compound(59.99, 10)
double_compound(9.99, 10)
