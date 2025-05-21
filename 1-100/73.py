class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        r=-1
        c=-1
        pr=[]
        for i in range(m):
            for j in range(n):
                if ((i!=r or j!=c) and matrix[i][j]==0):
                    pr.append([i,j])
                    r=i
                    c=j
                
            
        
        for x in pr :
            i=x[0]
            j=x[1]
           
            for a in range(m):
                if matrix[a][j]!=0:
                    matrix[a][j]=0
                
            
            for a in range(n):
                if matrix[i][a]!=0:
                    matrix[i][a]=0
                
            
