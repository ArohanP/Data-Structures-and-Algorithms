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

res=[]
