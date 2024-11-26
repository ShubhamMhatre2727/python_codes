def selection_sort(arr=[3, -2, 5,0,1], n=5):
    print(f"Befor sort: {arr}")
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if(arr[min_idx] > arr[j]):
                min_idx = j
        t = arr[min_idx]
        arr[min_idx] = arr[i]
        arr[i] = t
            
    print(f"After Sort: {arr}")

print("Selection Sort")
selection_sort()