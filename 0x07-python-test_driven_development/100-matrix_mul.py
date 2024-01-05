"""Mudule 100-matrix_mul
    Marecies multiplication
"""


def is_lists(mat, name):
    """Check if matrix is a list?
    """
    if not isinstance(mat, list):
        raise TypeError(f"{name} must be a list")


def is_list_of_lists(mat, name):
    """Check whether matrix is lists of lists?
    """
    if not all(isinstance(row, list) for row in mat):
        raise TypeError(f"{name} must be a list of lists")


def is_empty(mat, name):
    """Check whether a matrix is empty
    """
    if not len(mat) > 0 :
        raise ValueError(f"{name} can't be empty")
    for row in mat:
        if not len(row) > 0 :
            raise ValueError(f"{name} can't be empty")
    

def validate_elements(mat, name):
    """check if all elements of a matrix are of the correct type
    (float of int)
    """
    message = f"{name} should contain only integers or floats"
    for row in mat:
        for element in row:
            if not isinstance(element, int) and\
                not isinstance(element, float):
                raise TypeError(message)
def is_rectangle_matrix(mat, name):
    """Check of all rows of a matrix are the same size
    """
    if len(set(len(row) for row in mat)) != 1:
        raise TypeError(f"each row of {name} must be of the same size")


def validate_matrix(matrix, name):
    """Run check function to validate if object is
    valid matrix"""
    is_lists(matrix, name)
    is_list_of_lists(matrix, name)
    is_empty(matrix, name)
    validate_elements(matrix, name)
    is_rectangle_matrix(matrix, name)


def is_multiplicable(m_a, m_b):
    """Check if 2 matrecies can be multiplied together.

        Note: it assumes that each one is valid matrix
        all rows are of the same size.
    """
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


def matrix_mul(m_a, m_b):
    """Multiply 2 matrecies.

    Validate 2 matrecies to be matrecies and multiply them.
    Args:
        m_a: The first matrix.
        m_b: The second one.

    Return: A Result matrix.
    """
    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")
    is_multiplicable(m_a, m_b)

    a_rows, a_columns = len(m_a), len(m_a[0])
    b_rows, b_columns = len(m_b), len(m_b[0])

    c = [[] for _ in range(a_rows)]

    def get_dot_product(row, column):
        """"Get the dot product of to vectors.

            Args:
                row: the row number of the first matrix.
                column: The column number of the second.

            Return: The product.
        """
        product = 0
        # b_columns same as b_rows, rememeber?
        for i in range(a_columns):
            product += m_a[row][i] * m_b[i][column]

        return product

    for i in range(a_rows):
        for j in range(b_columns):
            c[i].append(get_dot_product(i, j))

    return c
