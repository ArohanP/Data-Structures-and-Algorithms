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
