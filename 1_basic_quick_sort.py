def quick_sort(array):
    """
    분할 정복을 이용한 퀵 정렬 재귀함수
    :param array:
    :return:
    """
    if(len(array)<2):
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

exam1 = [4, 2, 1, 7, 10]
print(quick_sort(exam1))
