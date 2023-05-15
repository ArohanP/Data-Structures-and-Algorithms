def fun3(n):
    if n==0:return
    fun3(int(n/2))
    print(n%2)

fun3(13)
