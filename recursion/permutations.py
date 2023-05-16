def fun(s):
    if len(s)==2:
        res_= []
        res_.append(s[0]+s[1])
        res_.append(s[1]+s[0])
        return res_
    else:
        for i in s:
            ans=fun(s.replace(i,""))
            for j in ans:
                res.append(i+j)
        return res
fun('abcd')
