def fibonacci(n):
    if (n==1)|(n==2):
        return n-1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

fibonacci(4)

def fib2(n):
    fib_arr=[]
    if n<=1:return n
    fib_arr.append(0)
    fib_arr.append(1)
    for i in range(2,n):
        fib_arr.append(fib_arr[i-1]+fib_arr[i-2])
    
    return fib_arr[n-1]

fib2(4)