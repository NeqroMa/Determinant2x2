def deter2x2(matrix):
    """
    function to calculate the determinant of
    the 2x2 matrix.
    The determinant of a matrix is defined as
    the upper-left element times the lower right element
    minus
    the upper-right element times the lower left element
    """
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    result = a*d - b*c
    # TODO: calculate the determinant of the 2x2 matrix

    return result
