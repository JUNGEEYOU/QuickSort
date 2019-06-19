def sum_func(arr):
    """

    :param arr:
    :return:
    """
    if len(arr) <1:
        return 0
    else:
        return arr[0] + sum_func(arr[1:])


arr1 = [1, 4, 5, 9]
print(sum_func(arr1))