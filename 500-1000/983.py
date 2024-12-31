class Solution(object):
    def mincostTickets(self, days, costs):
        dp0, dp1, dp2 = [costs[0]] * len(days) , [costs[1]] * len(days), [costs[2]] * len(days)
        for i in range(1, len(days)):
            dp0[i] = min(dp0[i - 1], dp1[i - 1], dp2[i - 1]) + costs[0]
            dp1[i] = dp0[i] - costs[0] + costs[1]
            dp2[i] = dp0[i] - costs[0] + costs[2]
            for j in range(0, i):
                if (days[i] - days[j] < 7): dp0[i] = min(dp0[i], dp1[j])
                if (days[i] - days[j] < 30): dp0[i] = min(dp0[i], dp2[j])
        return min(dp0[-1], dp1[-1], dp2[-1])

        
