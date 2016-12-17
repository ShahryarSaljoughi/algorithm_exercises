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
    :return: (i, j, max_sum) will be returned , i is the index of the start of Maximum-subarray,
     and j refers to the end of subarray,
     max_sum is the sum of the numbers of subarray
    """

    max_subarray = (0, 0)  # (i, j)
    max_sum = A[0]

    for i in range(len(A)):  # i is the start index
        for j in range(i, len(A)):  # j is the end index
            subarray_sum = compute_sum(A[i:j])
            if subarray_sum > max_sum:
                max_sum = subarray_sum
                max_subarray = (i, j)
    return max_subarray, max_sum

if __name__ == '__main__':
    a = eval(raw_input(">>input array. i.e: [1,-12, 10, 15, -2, 6]"))
    b = compute_maximum_subarray(a)
    print b