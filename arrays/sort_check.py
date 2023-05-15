def check_sorted(arr):
    is_sorted=True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            is_sorted=False
            break
    return is_sorted
check_sorted([1,2,3,4])