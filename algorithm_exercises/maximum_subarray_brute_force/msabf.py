__author__ = 'shahryar_saljoughi'


def compute_sum(A):
    """

    :param A: is of type list , containing numbers.
    :return: sum of the numbers in A will be returned .
    """
    result = 0
    for i in A:
        result += i
    return result


def compute_maximum_subarray(A):
    """

    :param A: A is a list , containing some numbers
    :return: (i, j) will be returned , i is the index of the start of Maximum-subarray,
     and j refers to the end of subarray
    """

    max_subarray = (0, 0)
    max_sum = A[0]

    for i in range(len(A)):
        for j in range(i, len(A)):
            sum = compute_sum(A[i:j])
            

