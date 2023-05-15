def fun2(n):
    if n==1:return 0
    else: return 1+fun2(int(n/2))
fun2(16)
