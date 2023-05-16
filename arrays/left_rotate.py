import reverse_array
def left_rotate(arr):
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr)-1]=temp
    return arr
left_rotate([1,2,3,4,5,6])
# Time complexity = Theta(n)
# Auxiliary Space = O(1) 

### Left rotate by d elements
def reverse_array_1(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr
def left_rotate_d(arr,d):
    reverse_array_1(arr,0,d-1)
    reverse_array_1(arr,d,len(arr)-1)
    reverse_array_1(arr,0,len(arr)-1)
    return arr
## Time Complexity - O(n)
## Space Complexity - O(1)

def left_rotate_d_alt(arr,d):
    arr_d=[]
    for i in range(d):
        arr_d.append(arr[i])
    print(arr_d)
    for i in range(len(arr)-d):
        arr[i]=arr[i+d]
    print(arr)
    k=len(arr_d)
    for i in range(len(arr_d)):
        arr[len(arr)-k]=arr_d[i]
        k-=1
    return arr

if __name__=="__main__":
    arr=[1,2,3,4,5]
    print(left_rotate_d_alt(arr,2))
