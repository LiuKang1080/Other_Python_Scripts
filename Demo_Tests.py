import math
from datetime import datetime


# print(math.sin(90 * (math.pi / 180)))


def ratio(num):
    """
    Convert minutes into decimal number. 15min = 0.25, 30min = 0.50, 45min = 0.75.
    :param num: Minutes.
    :return: Decimal number.
    """
    x = int(num) / 60
    print(x)

# ratio(45)

# values = [3, 6, 1, 5]
# index_min = min(range(len(values)), key = values.__getitem__)

# print(index_min)

# print(str(39.399999))
# print(chr(83))


def pythagorean_triplet():

    t0 = datetime.now()

    for c in range(1, 1000):
        for b in range(1, 1000):
            for a in range(1, 1000):
                if (a + b + c) == 1000 and ((a**2) + (b**2)) == (c**2) and a < b < c:
                    print(a, b, c)


    dt1 = datetime.now() - t0
    print(dt1)

pythagorean_triplet()
