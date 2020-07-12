# A. Make pythonic solutions for each of the following data structure
# and algorithm problems.
# f) Binary Search


def binary_search(list, low, high, find):
    while (low <= high):
        mid = low + (high - low) // 2

        if list[mid] == find:
            return mid

        elif list[mid] < find:
            low = mid + 1
        else:
            high = mid - 1

    return -1


list = [7, 15, 22, 33, 44, 55, 66]
low = 0
high = len(list) - 1

print(list)
find = int(input("Enter the number to find:"))

result = binary_search(list, low, high, find)

if(result == -1):
    print("Number is not present in the list.")
else:
    print("Number is present in the list in indefind:", result)
