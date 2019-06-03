def reverse_seq(n):
    num_list = []
    i = n
    while i <= n:
        num_list.append(i)
        i -= 1

        if i < 1:
            return num_list


print(reverse_seq(10))
