def partition(arr, l,h):
    pivot = h
    pointer = l - 1
    for i in range(l,h):
        if(arr[i] < arr[pivot]):
            pointer += 1
            (arr[pointer], arr[i]) = (arr[i], arr[pointer])
    (arr[pointer+1], arr[pivot]) = (arr[pivot], arr[pointer+1])
    return pointer+1

def quick_sort(arr=[8,7,6,1,0,9,2], l=0, h=6):
    print(f"Before Sort: {arr}")
    if(l<h):
        p = partition(arr, l, h)
        quick_sort(arr, l, p-1)
        quick_sort(arr, p, h)
    print(f"After Sort: {arr}")

# quick_sort([3,-2,5,0,1], 0, 4)
quick_sort()