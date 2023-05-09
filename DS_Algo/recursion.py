def fun1(n):
    if n==0:return
    fun1(n-1) 
    print(n)
    fun1(n-1)
Let's work out this function for n=3. fun1(3) will give - 
fun1(2) 
print(3)
fun1(2)
fun1(2) will give 

fun1(1)
print(2)
fun1(1)

fun1(1) will give 
fun1(0) - terminate
print(1) 
fun1(0) - terminate

implies fun1(1) will print(1)

implies fun1(2) will be 
1
2
1

implies the output of the function will be 

1
2
1
3
1
2
1

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

### Josephus problem without using recursion
def josephus(n,k):
    arr=list(range(1,n+1))
    pointer=0
    while(len(arr)>1):
        pointer=(pointer+k-1)%len(arr)
        del(arr[pointer])
        pointer=pointer%len(arr)
    return arr[pointer]
josephus(29,3)

## How to convert this into a recursive solution
# In the below function I try to convert the above written code to a recursive function.. Well, it is not the best solution...So, instead of using while loop as in the above code, 
#I use a function call for iteration and the stopping condition is provided by the function condition.
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

## Lucky numbers without a using recursion. Here, I am first creating an array arr of the numbers till n. Then, recursively I would delete the numbers as is the procedure to 
#find lucky numbers. The stopping criteria of the loop is till len(arr)>=i, because once len(arr)<n, we know that n is a lucky number and should just return 1. Inside the while
#loop the variable c exists to update the position of the array as the length of array is getting shorter in each iteration.

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


## This function uses recursion to tell whether a number is a lucky number or not. The logic is simple, in each iteration, the number n is shifted by n//count places.
#And then, the number will be eleiminated if at any step the last number in the series that is n is perfectly divisible by count. If count becomes more than the number n,
#we know that the number cannot be eliminated and the number n is a lucky number.

def is_lucky_recursion(n, count):
    if count > n:
        return True
    if n % count == 0:
        return False
    # Calculate next position of input after removing the count-th digit
    n = n - n // count
    return is_lucky_recursion(n, count + 1)
is_lucky_recursion(5,2)
#Let's work out an example with is_lucky_recursion(5,2) to get a better idea. We start the fucntion with count=2 because our process starts eliminating numbers from 2.
# I am writing is_lucky_recusion as fun from now on 
# 1 2 3 4 5 - initial.... 
# fun(5,2) - 1 2 3 4 5 becomes 1 3 5 so n=5 becomes n-n//2 i.e. 3
# fun(3,3) - 1 3 5 - five is eliminated because 5 is now 3 and 3%3==0 statisfies the if condition. so the function returns false because 5 is elimiated and its not a lucky number.

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
