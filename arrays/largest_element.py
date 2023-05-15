def largest_element(arr):
    max=arr[0]
    flag=0
    for i in range(len(arr)):
        if arr[i]>max:
            flag=i
            max=arr[i]
    return flag,max
largest_element([1,3,2,4])


