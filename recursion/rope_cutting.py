def rope_cutting(rope,a,b,c):
    if rope<=0:return rope
    return max((1+rope_cutting(rope-a,a,b,c)),(1+rope_cutting(rope-b,a,b,c)),(1+rope_cutting(rope-c,a,b,c)))
rope_cutting(5,2,5,1)
