__author__ = 'shahryar_saljoughi'


def max_subarray_linear_time(a_list):
    """
    C[i][j]  is a two-dimension array (actually it is a list of lists!),
     which contains the sum of values represented in a_list[i: j+1]---> i to j!
    :return: (i, j, sum) will be returned
    i is the index of start of subarray,
    j is the index of end of subarray,
    sum is the sum of the values present in the subarray
    """
    c = [[0 for j in range(len(a_list))] for i in range(len(a_list))]
    # initializing the main diagonal:
    for i in range(len(a_list)):
        c[i][i] = a_list[i]

    # .............................
    current_max_value = None  # this is supposed to have the value of some of max subarray
    current_i_j = None  # it is supposed to hold a tuple at last: I,J
    for j in range(1, len(a_list)):
        for i in range(j):
            c[i][j] = c[i][j-1] + a_list[j]
            if current_max_value is None or current_max_value < c[i][j]:
                current_max_value = c[i][j]
                current_i_j = i, j

    return current_i_j, current_max_value

if __name__ == '__main__':
    my_list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print max_subarray_linear_time(my_list)


"""
Unfortunately, this algorithm is of tetha(n^2)!!! so this is not a correct answere to exercise 4-1.5
"""