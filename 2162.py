class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        def cost(s):
            result = 0
            if startAt == int(s[0]):
                result += 0
            else:
                result += moveCost
            result += pushCost
            for i in range(1, len(s)):
                if s[i - 1] == s[i]:
                    result += pushCost
                else:
                    result += moveCost
                    result += pushCost
            return result

        M = targetSeconds // 60
        nums = []
        for i in range(M , -1, -1):
            if targetSeconds - i * 60 < 100:
                a = str(i)
                b = str(targetSeconds - i * 60)
                if b == '0':
                    r = a + '00'
                elif len(b) == 1:
                    r = a + '0' + b
                else:
                    r = a + b
                if len(r)<=4:
                    nums.append(r.lstrip('0'))
            else:
                break
        result = float('inf')

        for r in nums:
            result = min(result, cost(r))
        return result
		
