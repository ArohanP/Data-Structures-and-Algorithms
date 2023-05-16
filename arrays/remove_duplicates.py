## Remove duplicates from a sorted array
def remove_duplicates(arr):
    array_map={}
    for i in range(len(arr)):
        if arr[i] not in array_map.keys():
            array_map[arr[i]]=1
        else:
            array_map[arr[i]]+=1
    for i in range(len(arr)):
        try:
            if array_map[arr[i]]>1:
                del(arr[i])
        except:
            return arr
remove_duplicates(['a','a','b'])

def remove_duplicates_sorted_array(arr):
    temp=0
    for i in range(1,len(arr)):
        print(i)
        try:
            if arr[i]==arr[temp]:
                j=i
                while arr[j]==arr[temp]:
                    del(arr[j])
                temp+=1    
        except:
            return arr
remove_duplicates_sorted_array([1,1,2,2,2,3,4])