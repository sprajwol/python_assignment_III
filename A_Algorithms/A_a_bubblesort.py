# A. Make pythonic solutions for each of the following data structure
# and algorithm problems.
# a) Bubble Sort


def bubble_sort(list):
    num = len(list)

    for i in range(num-1):
        for j in range(num-i-1):

            if (list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]


list = [33, 44, 55, 22, 15, 66, 7]

bubble_sort(list)
print(list)
