__author__ = 'shahryar_saljoughi'


def find_max_crossing_subarray(a_list, low, mid, high):

    #########
    left_sum = None
    sum = 0
    max_left = None
    for i in range(mid, low - 1, -1):
        sum = sum + a_list[i]
        if left_sum is None or sum > left_sum:
            left_sum = sum
            max_left = i

    #########
    right_sum = None
    sum = 0
    max_right = None
    # a_list[:high] --> won't include a_list[high]. So we'll use a_list[high + 1]  :
    for j in range(mid + 1, high + 1):
        sum = sum + a_list[j]
        if right_sum is None or right_sum < sum:
            right_sum = sum
            max_right = j

    # return max_left, max_right, left_sum + right_sum
    return max_left, max_right, left_sum + right_sum


def find_max_subarray(a_list, low, high):
    if low == high:
        return low, high, a_list[low]
    else:
        mid = (low + high)/2
        left_result = find_max_subarray(a_list, low, mid)
        right_result = find_max_subarray(a_list, mid+1, high)
        cross_result = find_max_crossing_subarray(a_list, low, mid, high)

        # max_subarray = max(left_result[-1], right_result[-1], cross_result[-1])
        # return left_result, right_result,  cross_result
        if left_result[-1] > right_result[-1] and \
           left_result[-1] > cross_result[-1]:
            return left_result
        elif right_result[-1] > left_result[-1] and\
                right_result[-1] > cross_result[-1]:
            return right_result
        else:
            return cross_result


if __name__ == "__main__":
    my_list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    my_list_2 = [13, -2, 7, -20]
    print find_max_subarray(my_list, low=0, high=len(my_list)-1)
    print find_max_subarray(my_list_2, 0, len(my_list_2)-1)