# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr) - 1):
        # index for current and the index to swap w/ the smallest
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for l in range(i+1, len(arr)):
            if arr[l] < arr[smallest_index]:
                smallest_index = l

        # TO-DO: swap
        # after we find smallest elem, swap it w/ elm on the right edge.
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # cant compare the last num cos theres nothing after it
    indexing_length = len(arr) - 1
    # sorted variable as exit when sorting is complete
    sorted = False

    # while sorted is false, do this:
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            # if left is < than right
            if arr[i] > arr[i+1]:
                # sorted is false
                sorted = False
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


'''
x
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
x
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
