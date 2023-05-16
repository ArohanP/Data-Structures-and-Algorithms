def fun7(n):
    if n==0:return 1
    return n*fun7(n-1)

fun7(4)

def fun8(n,k):
    if (n==0)|(n==1):return k
    else:
        return fun8(n-1,k*n)
print(fun8(4,1))