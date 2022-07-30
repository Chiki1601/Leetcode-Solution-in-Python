class Solution(object):
    def getPermutation(self, n, k):
        pe=[]
        list=[]
        for i in range(1,n+1):
            list.append(str(i))
        k1=k-1
        n1=n-1
        def fact(m):
            if m==0:
                return 1
            x=1
            for i in range(1,m+1):
                x=x*i
            return x
        while n1>=0:
            a=min(k1/fact(n1),n1)
            
            k1=k1-a*fact(n1)
            n1=n1-1
            pe.append(list[a])
            list.pop(a)
            
        return ''.join(pe)
