### Find the number of subsets of an array of a given count ----

def countsubsets(arr,n,sum):
    if n==0:
        if sum==0:return 1
        else: return 0
    else:
        return countsubsets(arr,n-1,sum-arr[n-1])+countsubsets(arr,n-1,sum)

