# A. Make pythonic solutions for each of the following data structure
# and algorithm problems.
# i) Tower of Hanoi problem for ‘n’ number of disks.


def tower_of_hanoi(n, source, destination, mid):
    if (n == 1):
        print(
            f"Move disk {n} from source: {source} to destination: {destination}.")
        return

    tower_of_hanoi(n-1, source, mid, destination)
    print(
        f"Move disk {n} from source: {source} to destination: {destination}.")
    tower_of_hanoi(n-1, mid, destination, source)


n = int(input("Enter number of rings in tower of hanoi:"))
source = "A"
mid = "B"
destination = "C"
tower_of_hanoi(n, source, destination, mid)
