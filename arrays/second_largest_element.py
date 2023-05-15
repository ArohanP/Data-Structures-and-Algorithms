def second_largest(arr):
    max=arr[0]
    flag_1=0
    flag_2=0
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
            flag_2=flag_1
            flag_1=i
    return flag_2
second_largest([1,3,2,4])
