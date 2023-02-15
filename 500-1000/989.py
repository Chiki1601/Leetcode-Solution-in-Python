class Solution(object):
    def addToArrayForm(self, num, k):
        res = [] 
        i=len(num)-1
        while i >= 0 or k:
            if i >= 0:
                k += num[i]
            res.insert(0, k%10)
            k = k/10
            i -= 1
        return res
