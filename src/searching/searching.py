def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    begin_index = 0
    # -1 cos Python starts at 0
    end_index = len(arr) - 1
    # while BI value is lower than EI
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        # return value instead of midpoint position
        midpoint_value = arr[midpoint]
        if midpoint_value == target:
            return midpoint
        # target on L
        elif target < midpoint_value:
            # EI is L of midpoint
            end_index = midpoint - 1
        # else if the target is > the midpoint
        else:
            begin_index = midpoint + 1

    return -1  # not found.
