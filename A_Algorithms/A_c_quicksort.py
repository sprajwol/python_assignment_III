# A. Make pythonic solutions for each of the following data structure
# and algorithm problems.
# c) Quick Sort


def quick_sort(list, low, high):

    if (low < high):
        pi = partitioning(list, low, high)

        quick_sort(list, low, pi - 1)
        quick_sort(list, pi + 1, high)


def partitioning(list, low, high):
    i = low-1
    pivot = list[high]

    for j in range(low, high):
        if list[j] < pivot:
            i = i+1
            list[i], list[j] = list[j], list[i]

    list[i+1], list[high] = list[high], list[i+1]
    return i+1


list = [33, 44, 55, 22, 15, 66, 7]
low = 0
high = len(list)-1
quick_sort(list, low, high)
print(list)
