# Given a list of numbers find the highest and second highest numbers.


def highest_numbers(arr):
    max_num = [arr[0]]

    if arr[0] > arr[1]:
        max_num.append(arr[1])
    else:
        max_num.insert(arr[1], 0)

    for i in range(1, len(arr)):
        if arr[i] > max_num[1]:
            if arr[i] > max_num[0]:
                max_num[1] = max_num[0]
                max_num[0] = arr[i]
            else:
                max_num[1] = arr[i]

    return max_num


def second_high(arr):
    a = 0
    b = 0
    for num in arr:
        if num > a:
            a = num
        if num < a and num > b:
            b = num
    return a, b


def built_ins(arr, n):
    max_num = []
    arr.sort()

    for i in range(1, n + 1):
        max_num.append(arr[-i])

    return max_num


my_list = [1, 10, 55, 982, 6, 592, 0, 62]
print(highest_numbers(my_list))
print(built_ins(my_list, 3))
print(second_high(my_list))

# Test to see if for loops still work (...They do!)
for i in range(0, 5):
    print("iteration number " + str(i))
