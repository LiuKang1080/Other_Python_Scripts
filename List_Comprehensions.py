L1 = [1, 2, 3]
L2 = [10, 20, 30]

# General syntax for list comprehensions are [<expression> for <varname> in <iterable>]
print([x+y for x, y in zip(L1, L2)])
