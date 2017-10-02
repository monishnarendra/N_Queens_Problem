import copy

def take_input():
    while True:
        try:
            size = int(input('Enter the size of the chessboard?'))
            if size <= 3:
                print("Enter a value such that size>=4")
                continue
            return size
        except ValueError:
            print("Invalid value entered. Enter again")

def get_board(size):
    board = [0] * size
    for ix in range(size):
        board[ix] = [0] * size
    return board

def print_solutions(solutions, size):
    for sol in solutions:
        for row in sol:
            print(row)
        print()

def is_safe(board, row, col, size):
    for iy in range(col):
        if board[row][iy] == 1:
            return False

    ix, iy = row, col
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == 1:
            return False
        ix -= 1
        iy -= 1

    jx, jy = row, col
    while jx < size and jy >= 0:
        if board[jx][jy] == 1:
            return False
        jx += 1
        jy -= 1

    return True

def solve(board, col, size):
    if col >= size:
        return

    for i in range(size):
        if is_safe(board, i, col, size):
            board[i][col] = 1
            if col == size - 1:
                add_solution(board)
                board[i][col] = 0
                return
            solve(board, col + 1, size)
            # backtrack
            board[i][col] = 0


def add_solution(board):
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)

size = take_input()
board = get_board(size)
solutions = []
solve(board, 0, size)
print_solutions(solutions, size)

print("Total solutions = {}".format(len(solutions)))