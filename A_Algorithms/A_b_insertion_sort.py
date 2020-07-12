# A. Make pythonic solutions for each of the following data structure
# and algorithm problems.
# b) Insertion Sort


def insertion_sort(list):
    num = len(list)

    for i in range(1, num):
        key = list[i]

        j = i-1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


list = [33, 44, 55, 22, 15, 66, 7]

insertion_sort(list)
print(list)
