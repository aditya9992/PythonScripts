import sys

arr = [int(s) for s in sys.argv[1].split(',')]

def binary_search(arr, item):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == item:
            return mid
        else:
            if item < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
