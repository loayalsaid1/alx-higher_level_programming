"""Try a solution for it inspired by the
    Back To Back SWE channel video about the problem
    Here is the link: https://youtu.be/wGbuCyNpxIg
"""


def is_valid_position(current_columns):
    row = len(current_columns) - 1
    for i in range(row):
        diff = abs(current_columns[row] - current_columns[i])
        if diff == 0 or diff == row - i:
            return False
    
    return True


def solve_n_queens(n, row, current_columns):
    if row == n:
        solutions.append(current_columns.copy())
        return

    for column in range(n):
        current_columns.append(column)
        if is_valid_position(current_columns):
            solve_n_queens(n, row+1, current_columns)
        current_columns.pop()
    


solutions = []

solve_n_queens(4, 0, [])
for x in solutions:
    print(x)
