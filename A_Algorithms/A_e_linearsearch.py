# A. Make pythonic solutions for each of the following data structure
# and algorithm problems.
# e) Linear Search


def linear_search(list, find):
    n = len(list)

    for i in range(0, n):
        if (list[i] == find):
            return i
    return -1


list = [33, 44, 55, 22, 15, 66, 7]
print(list)
find = int(input("Enter the number to find:"))

result = linear_search(list, find)

if(result == -1):
    print("Number is not present in the list.")
else:
    print("Number is present in the list in index:", result)
