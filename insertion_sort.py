def insertion_sort(arr=[3, -2, 5,0,1], n=5):
    print(f"Befor sort: {arr}")
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
            
    print(f"After Sort: {arr}")

print("Insertion Sort")
insertion_sort()