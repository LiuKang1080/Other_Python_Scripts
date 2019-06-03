"""
Diagonal.py - Given a fixed point (row, col) that is in a nested list, find both the forward and backward diagonals about the center.
"""

# Nested list given as below.
# Remember that rows and cols start at index 0

my_list = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            ['H', 'I', 'J', 'K', 'L', 'M', 'N'],
            ['O', 'P', 'Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z', '1', '2'],
            ['3', '4', '5', '6', '7', '8', '9'],
            ['!', '@', '#', '$', '%', '^', '&']
          ]

my_list2 = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
           ]


def backwards_diagonal_check(row_num, col_num, board):

    row = row_num
    col = col_num

    # here are the indices of the 'board' provided and stored into a var named diagonal.
    diagonal = [board[row][col]]
    print(" Your point is:", diagonal)

    i = 1

    while True:
        try:
            diagonal.append(board[row + i][col + i])
        except IndexError:
            break

        i += 1
    # Here the while is always True, it's never false, the break is the only way out of the loop and that arises when we
    # get an out of bounds index error, we keep adding +1 to row and col in each iteration.

    i = 1

    while True:
        if min([row - i, col - i]) >= 0:
            try:
                diagonal.insert(0, board[row - i][col - i])
            except IndexError:
                break
        else:
            break
        i += 1

    diagonal = ''.join(i if i else 'N' for i in diagonal)
    print(diagonal)


def forwards_diagonal_check(row_num, col_num, board):

    row = row_num
    col = col_num

    # Here are the indices of the 'board' provided and stored into a var named diagonal.
    diagonal = [board[row][col]]
    print(" Your point is:", diagonal)

    i = 1

    while True:
        if col - i >= 0:
            try:
                diagonal.append(board[row + i][col - i])
            except IndexError:
                break
        else:
            break
        i += 1
    i = 1

    while True:
        if row - i >= 0:
            try:
                diagonal.insert(0, board[row - i][col + i])
            except IndexError:
                break
        else:
            break
        i += 1

    diagonal = ''.join(i if i else 'N' for i in diagonal)
    # Here is comprehensions, where this says for i in diagonal: if i is True then .join with the delimiter of '',
    # else join 'N' rather than i.
    print(diagonal)


backwards_diagonal_check(1, 1, my_list)
backwards_diagonal_check(0, 1, my_list2)

forwards_diagonal_check(1, 2, my_list)
forwards_diagonal_check(0, 1, my_list2)
