def reverse_array(arr):
    pointer1=0
    pointer2=len(arr)-1
    while pointer1<pointer2:
        arr[pointer1],arr[pointer2]=arr[pointer2],arr[pointer1]
        pointer1+=1
        pointer2-=1
    return arr
reverse_array([1,2,3,4,5])