import sys


arr = [int(s) for s in sys.argv[1].split(',')]


def quick_sort(array):
    quick_sort_helper(array, 0, len(array)-1)

def quick_sort_helper(array, low, high):
    if(low<high):
        pivot_loc = partition(array,low,high)
        quick_sort_helper(array, low, pivot_loc - 1)
        quick_sort_helper(array, pivot_loc + 1, high)



def partition(array, low, high):
    pivot = array[low]
    left = low + 1
    last = high

    done = False

    while not done:
        while left <=last and array[left] <= pivot:
              left = left + 1
        while array[last] >= pivot and last >= left:
                last = last - 1

        if(last < left):
            done = True
        else:
            temp = array[left]
            array[left] = array[last]
            array[last] = temp

    temp = array[low]
    array[low] = array[last]
    array[last] = temp

    return last

quick_sort(arr)

print(arr)