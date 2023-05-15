def lucky_numbers(n):
    arr=list(range(1,n+1))
    i=2
    while len(arr)>=i:
        c=1
        k=len(arr)
        for j in range(i,k+1,i):
            del(arr[j-c])
            c+=1
        if n not in arr:
            return 1
        i+=1
    return 0
lucky_numbers(135)

def is_lucky_recursion(n, count):
    if count > n:
        return True
    if n % count == 0:
        return False
    # Calculate next position of input after removing the count-th digit
    n = n - n // count
    return is_lucky_recursion(n, count + 1)
is_lucky_recursion(5,2)

