class Solution:
    def applyOperations(self, n):

        # apply the first part of operations
        for i in range(1,len(n)):
            if n[i] == n[i-1]:
                n[i-1], n[i] = n[i-1]*2, 0    
        
        # 'not' of any non-zero number is equal to 0, i.e.,
        # less than 'not 0' which is 1 (here, sorting is stable)
        return sorted(n, key=lambda x: not x)
