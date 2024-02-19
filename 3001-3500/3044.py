import math
 
class Solution:

  def _is_prime(self, n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

  def mostFrequentPrime(self, M: List[List[int]]) -> int:
    nums = defaultdict(int)
    Y, X = len(M), len(M[0])
    for y in range(Y):
      for x in range(X):
        for dy, dx in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
          y_, x_ = y, x
          v = M[y][x]
          while Y > y_ + dy >= 0 and X > x_ + dx >= 0:
            y_ += dy
            x_ += dx
            v = v * 10 + M[y_][x_]
            if self._is_prime(v):
              nums[v] += 1

    if not nums:
      return -1
    
    cnt, res = max(nums.values()), 0
    for v, c in nums.items():
      if c == cnt:
        res = max(res, v)
    
    return res
