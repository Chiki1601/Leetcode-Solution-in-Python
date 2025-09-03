class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        points.sort(key = lambda x: (x[0],-x[1]))
        ans = 0
        for i in range(n-1):
            x1,y1 = points[i]
            y_limit = float("-inf") 
            for j in range(i+1,n):
                x2,y2 = points[j]
                if y2<=y1 and y2>y_limit:
                    y_limit = y2
                    ans+=1
        

        return ans
