board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def show_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(0, len(brd[i])):
            if j % 3 == 0 or j == 0:
                print(" | " + str(brd[i][j]), end=" ")
            else:
                print(brd[i][j], end="\n" if j == 8 else " ")


def find_blank(brd):
    for i in range(len(brd)):
        for j in range(len(brd[i])):
            if brd[i][j] == 0:
                return (i,j)
    return False


def check_valid(brd, value, position):
    row = position[0] // 3 * 3  # starting row
    col = position[1] // 3 * 3  # starting col

    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if brd[i][j] == value and (i, j) != position:
                return False

    for i in range(len(brd[position[0]])):
        if brd[position[0]][i] == value and position[1] != i:
            return False

    for i in range(len(brd)):
        if brd[i][position[1]] == value and position[0] != i:
            return False

    return True


def backtrack(brd):
    if find_blank(brd):
        row, col = find_blank(brd)
        for i in range(1, 10):  # there are 9 possible value ranging from 1 to 9
            if check_valid(brd, i, (row, col)):  # try to insert all the possible value
                brd[row][col] = i  # if the value meets the requirements, set the value
                if backtrack(brd):  # proceed to the next blank box to find the value
                    return True  # return true means the problem has been solve
                else:
                    brd[row][col] = 0  # reset the value to 0 and try with another possibility

    else:
        return True  # return true if no other blank is found

    return False  # return False when all the possibilities failed to meet the requirements

show_board(board)
solved = backtrack(board)

print("Solved" if solved else "Unsolved")

show_board(board)



