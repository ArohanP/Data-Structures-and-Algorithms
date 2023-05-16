def palidrome_check(string,first,last):
    if first>=last:return True
    return (string[first]==string[last])&(palidrome_check(string,first+1,last-1))
palidrome_check('abaa',0,3)    
