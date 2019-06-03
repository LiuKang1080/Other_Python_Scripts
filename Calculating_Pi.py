# Generate an infinite sequence of odd numbers, starting at 1. Do this first before calculating pi.
# Sequence = 4 + 4/3 - 4/5 + 4/7 - 4/9 + 4/11 ...


# Odd sequence generator
def odd_sequence_generator(n):
    a = 1
    while a < n:
        yield a
        a += 2

# for i in odd_sequence_generator(100):
#     print(i)


# Calculate approximation of pi
def pi_calculation(num):
    odd_num = odd_sequence_generator(num)
    pi_approximation = 0

    count = 1
    while count < num:
        pi_approximation += (4 / next(odd_num))
        yield pi_approximation
        pi_approximation -= (4 / next(odd_num))
        yield pi_approximation

        count += 1


for i in pi_calculation(1000):
    print(i)
