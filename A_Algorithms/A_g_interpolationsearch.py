# A. Make pythonic solutions for each of the following data structure
# and algorithm problems.
# g) Interpolation Search


def interpolation_search(list, low, high, find):
    while (low <= high and find >= list[low] and find <= list[high]):
        if (low == high):
            if (list[low] == find):
                return low
            return -1

        pos = low + \
            int(((float(high - low) /
                  (list[high] - list[low])) * (find - list[low])))

        if list[pos] == find:
            return pos

        if list[pos] < find:
            low = pos + 1

        else:
            high = pos - 1

    return -1


list = [7, 15, 22, 33, 44, 55, 66]
low = 0
high = len(list) - 1

print(list)
find = int(input("Enter the number to find:"))

result = interpolation_search(list, low, high, find)

if(result == -1):
    print("Number is not present in the list.")
else:
    print("Number is present in the list in indefind:", result)
