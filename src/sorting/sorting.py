# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    a = 0
    b = 0
     
    # starting at the beginning of `a` and `b`
    while len(merged_arr) < elements:
        if arrA[a] <= arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1
        # compare the next value of each
        if a == len(arrA) or b == len(arrB):
            merged_arr.extend(arrA[a:] or arrB[b:])

    # add smallest to `merged_arr`

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    middle = 0
    left = 0
    right = 0
    if len(arr) > 1:
        #divide array 
        middle = len(arr) // 2
        # recursively call merge_sort() on LHS
        left = merge_sort(arr[:middle])
        # recursively call merge_sort() on RHS
        right = merge_sort(arr[middle:])
        # merge sorted pieces
        arr = merge(left, right)    
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

