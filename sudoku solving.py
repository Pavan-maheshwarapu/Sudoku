def is_valid(puzzle, row, col, guess):
    # Check if the number already exists in the row
    # figures out whether the guess at the row/column of the puzzle is a valid guess
    # returns True if it is valid, else false

    # staring with row
    for i in range(9):
        if puzzle[row][i] == guess:
            return False

    # Check if the number already exists in the column
    for i in range(9):
        if puzzle[i][col] == guess:
            return False

    # Check if the number already exists in the 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[start_row + i][start_col + j] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                for guess in range(1, 10):
                    if is_valid(puzzle, row, col, guess):
                        puzzle[row][col] = guess

                        # Recursively solve the puzzle
                        if solve_sudoku(puzzle):
                            return True

                        # Backtrack and try a different number
                        puzzle[row][col] = -1

                # No valid number found, backtrack to the previous cell
                return False

    # All cells are filled, puzzle solved
    return True


# Example Sudoku puzzle
puzzle = [
    [3, 9, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],

    [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    [2, -1, 6, -1, -1, 3, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],

    [5, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, 7, -1, 1, -1, 5, -1, 4, -1],
    [1, -1, 9, -1, -1, -1, 2, -1, -1]

]

if solve_sudoku(puzzle):
    print("Solved sudoku can be given as!!")
    for row in puzzle:
        print(row)
else:
    print("Given sudoku puzzle is unsolvable")




