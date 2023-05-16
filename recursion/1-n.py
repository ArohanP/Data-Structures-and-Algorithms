def fun6(n,i):
    if i>n:return
    print(i)
    fun6(n,i+1)
fun6(10,1)