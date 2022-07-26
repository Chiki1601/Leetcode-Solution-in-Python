class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0]*n for _ in range(m)]
        for i,j in guards:
            grid[i][j] = 2
        for i,j in walls:
            grid[i][j] = 2
        for i,j in guards:
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                x = i+dx
                y = j+dy
                while 0<=x<m and 0<=y<n and (grid[x][y]==0 or grid[x][y]==1):
                    grid[x][y] = 1
                    x += dx
                    y += dy
        return sum(grid[i][j]==0 for i in range(m) for j in range(n))   
