def josephson(n,k):
    arr=list(range(1,n+1))
    pointer=0
    while(len(arr)>1):
        pointer=(pointer+k-1)%len(arr)
        del(arr[pointer])
        pointer=pointer%len(arr)
    return arr[pointer]
josephson(29,3)

## How to convert this into a recursive solution

def joseph(arr,pointer,k):
    if len(arr)==1:
        print(arr[0])
    else:
        pointer=(pointer+k-1)%len(arr)
        del(arr[pointer])
        pointer=pointer%len(arr)
        joseph(arr,pointer,k)
joseph([0,1,2,3,4],0,3)

def recursive_jos(n,k):
    if n==1: return 0
    else:
        return ((recursive_jos(n-1,k)+k)%n)
recursive_jos(5,3)
