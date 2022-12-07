class Solution(object):
    def bestClosingTime(self, customers):
        n = len(customers)
        penalty = customers.count('Y')
        if penalty == n: 
            return n
        min_, ans = n, 0
        for index, value in enumerate(customers):
            if min_ > penalty:
                min_ = penalty
                ans = index
            if value == 'Y':
                penalty -= 1
            else:
                penalty += 1
        if min_ > penalty: return n
        return ans
