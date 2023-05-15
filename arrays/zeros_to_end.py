def zeros_to_end(arr):
    pointer1=0
    pointer2=len(arr)-1
    print(pointer2)
    while pointer1<pointer2:
        if arr[pointer1]==0:
            if arr[pointer2]==0:
                pointer2-=1
            arr[pointer1],arr[pointer2]=arr[pointer2],arr[pointer1]
            pointer2-=1
        pointer1+=1
    return arr
zeros_to_end([2,3,4,0,5,0,6,7,0,8,0,0,0,0,10,10,9,11,0,23,45])