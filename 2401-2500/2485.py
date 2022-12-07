class Solution:
    def pivotInteger(self, n: int) -> int:
        l = []
        for a in range(1,n+1):
            l.append(a)
            #print(l)
        for a in range(n,0,-1):
            if sum(l[a:])==sum(l[:a-1]):
                return a
                continue 
        return 1
