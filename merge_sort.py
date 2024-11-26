def merge_sort(arr):
    if(len(arr)>1):
        r = len(arr)//2
        L = arr[:r]
        R = arr[r:]

        merge_sort(L)
        merge_sort(R)

        idx=idx1=idx2=0

        while(idx1 < len(L) and idx2 < len(R)):
            if(L[idx1] < R[idx2]):
                arr[idx] = L[idx1]
                idx1 += 1
            else:
                arr[idx] = R[idx2]
                idx2 += 1
            idx += 1
        
        while(idx1<len(L)):
            arr[idx] = L[idx1]
            idx1 += 1
            idx += 1
        
        while(idx2 < len(R)):
            arr[idx] = R[idx2]
            idx2 += 1
            idx += 1

        return arr
        

arr = [3,-2,5,0,1]
print(f"Before Sort: {arr}")
arr = merge_sort(arr)
print(f"After Sort: {arr}")