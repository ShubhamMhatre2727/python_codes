def bubble_sort(arr=[3, -2, 5,0,1], n=5):
    print(f"Befor sort: {arr}")
    for i in range(n):
        for j in range(1, n-i):
            if(arr[j-1] > arr[j]):
                t = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = t
    print(f"After Sort: {arr}")

print("Bubble Sort")
bubble_sort()