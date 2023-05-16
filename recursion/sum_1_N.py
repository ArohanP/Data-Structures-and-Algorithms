def sum_1_N(n):
    if n==0:return 0
    else:
        return n+sum_1_N(n-1)
sum_1_N(4)