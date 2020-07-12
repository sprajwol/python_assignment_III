# A. Make pythonic solutions for each of the following data structure
# and algorithm problems.
# d) Merge Sort


def merge_sort(list):
    if len(list) > 1:
        n = len(list)
        mid = n // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]

                i += 1
            else:
                list[k] = right[j]

                j += 1

            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


list = [33, 44, 55, 22, 15, 66, 7]
merge_sort(list)
print(list)
