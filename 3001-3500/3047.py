
class Solution:
    class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        ans = 0
        n = len(bottomLeft)
        for i in range(n):
            firstRectBL = bottomLeft[i]
            firstRectTR = topRight[i]
            for j in range(i + 1, n):
                secondRectBL = bottomLeft[j]
                secondRectTR = topRight[j]
                if secondRectBL[0] >= firstRectTR[0] or secondRectTR[0] <= firstRectBL[0]:
                    continue
                if secondRectTR[1] <= firstRectBL[1] or secondRectBL[1] >= firstRectTR[1]:
                    continue
                pntAx = max(firstRectBL[0], secondRectBL[0])
                pntAy = max(firstRectBL[1], secondRectBL[1])
                pntBx = min(firstRectTR[0], secondRectTR[0])
                pntBy = min(firstRectTR[1], secondRectTR[1])
                sideA = pntBx - pntAx
                sideB = pntBy - pntAy
                ans = max(ans, min(sideA, sideB))
        return ans ** 2
        
