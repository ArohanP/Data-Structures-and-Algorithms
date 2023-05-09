def fun1(n):
    if n==0:return
    fun1(n-1) 
    print(n)
    fun1(n-1)
fun1(2)

def fun2(n):
    if n==1:return 0
    else: return 1+fun2(int(n/2))
fun2(16)
fun2(17)

def fun3(n):
    if n==0:return
    fun3(int(n/2))
    print(n%2)

fun3(13)

def fun4(n):
    if n==0:return
    print(n)
    fun4(n-1)

fun4(10)

def fun5(n):
    if n==0:return 
    fun5(n-1)
    print(n)
fun5(10)


def fun6(n,i):
    if i>n:return
    print(i)
    fun6(n,i+1)
fun6(10,1)

def fun7(n):
    if n==0:return 1
    return n*fun7(n-1)

fun7(4)

def fun8(n,k):
    if (n==0)|(n==1):return k
    else:
        return fun8(n-1,k*n)
print(fun8(4,1))
 

def factorial(n):
    if n==1:return 1
    else:
        return n*factorial(n-1)

factorial(4)


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

def sum_1_N(n):
    if n==0:return 0
    else:
        return n+sum_1_N(n-1)
sum_1_N(4)

def palidrome_check(string,first,last):
    if first>=last:return True
    return (string[first]==string[last])&(palidrome_check(string,first+1,last-1))
palidrome_check('abaa',0,3)    

def sum_of_digits(n):
    if n==0:return 0
    return sum_of_digits(int(n/10))+n%10
sum_of_digits(253)
    
def rope_cutting(rope,a,b,c):
    if rope<=0:return rope
    return max((1+rope_cutting(rope-a,a,b,c)),(1+rope_cutting(rope-b,a,b,c)),(1+rope_cutting(rope-c,a,b,c)))
rope_cutting(5,2,5,1)

def generate_subsets(s):
    if len(s) == 0:
        return [[]]
    else:
        subsets = generate_subsets(s[1:])
        return subsets + [[s[0]] + subset for subset in subsets]
generate_subsets('abc')

def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Move disk 1 from {from_rod} to {to_rod}")
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from {from_rod} to {to_rod}")
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

# Example usage
tower_of_hanoi(3, 'A', 'C', 'B')

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


### Find the number of subsets of an array of a given count ----

def countsubsets(arr,n,sum):
    if n==0:
        if sum==0:return 1
        else: return 0
    else:
        return countsubsets(arr,n-1,sum-arr[n-1])+countsubsets(arr,n-1,sum)

### Given a number return the number raised to its reverse

def pow(num,rev):
    if rev==0: return 1
    else:
        return num*pow(num,rev-1)

pow(11,11)

def sum_of_digits(num):
    if num==0:return 0
    return (num%10) + sum_of_digits(int(num/10))

sum_of_digits(101145)

#### find the digital root of a number

def digital_root(num):
    if int(num/10)==0:
        return num 
    else:
        return digital_root(sum_of_digits(num))

digital_root(45)

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

print(6 - int(6/5))

def is_lucky_recursion(n, count):
    if count > n:
        return True
    if n % count == 0:
        return False
    # Calculate next position of input after removing the count-th digit
    n = n - n // count
    return is_lucky_recursion(n, count + 1)
is_lucky_recursion(5,2)

## Print all the possible words from phone digits ----

class Solution:
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        #Your code here
        d={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res=[]
        def backtrack(i,curr):
            if i>=N:

                res.append(curr)

                return

            keyval=d[a[i]]

            for j in keyval:

                curr+=j

                backtrack(i+1,curr)

                curr=curr[:-1]

        backtrack(0,"")

        return res
sol=Solution()  
sol.possibleWords([2,3],2)  
curr='abc'
curr=curr[:-1]
curr