__author__ = 'edfeng'


def quick_sort(array):
    greater = []
    less = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for e in array:
        if e <= pivot:
            less.append(e)
        else:
            greater.append(e)
    return quick_sort(less) + [pivot] + quick_sort(greater)