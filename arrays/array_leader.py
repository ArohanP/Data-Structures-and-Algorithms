def array_leader(arr):
    curr_leader=arr[len(arr)-1]
    print(curr_leader)
    i=len(arr)-2
    while i>=0:
        if arr[i]>curr_leader:
            print(arr[i])
            curr_leader=arr[i]
        i-=1
    return
if __name__=="__main__":
    arr=[2,3,4,1,2,0]
    array_leader(arr)