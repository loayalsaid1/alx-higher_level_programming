#!/usr/bin/python3
"""Implement a solution to the nqueens buzzle.

    You will have to place N queens in a N x N chess board
    in posistions so no queen can attack the other.
"""


def solve_n_queens(n, row_number, used_columns):
    """solve_n_queens => recursive function to solve
    nQueens buzzle.

        Args:
            n: the number of rows and columns of the board
                and number of queens to place.
            row_number: the current row we are operating on.
            used_columns: an array of ints refering to the positions
                of previously placed queens

        Return void
    """
    # Base case => Your goal
    if row_number == n:
        indecies.append(used_columns.copy())
        return

    for i in range(n):
        used_columns.append(i)
        if is_valid_position(used_columns):
            solve_n_queens(n, row_number+1, used_columns)
        used_columns.pop()


def is_valid_position(used_columns):
    """Check if the posisions of queens in each row
    is valid posisions

        Args:
            used_columns: a list of the columns of queens placed so far

        Return: Boolean value indicating the answer
    """
    row = len(used_columns) - 1
    for i in range(row):
        diff = abs(used_columns[row] - used_columns[i])
        if diff == 0 or diff == (row - i):
            return False

    return True


if __name__ == "__main__":
    from sys import argv as argv

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    indecies = []
    solve_n_queens(n, 0, [])
    solutions = []
    for index in indecies:
        solution = []
        for i in range(n):
            solution.append([i, index[i]])
        print(solution)
