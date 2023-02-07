class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        j = 0
        dic = {}
        maxlen = -float('inf')
        for i in range(len(tree)):
            if tree[i] not in dic:
                dic[tree[i]] = 1
            else:
                dic[tree[i]] += 1
            while len(dic) > 2:
                dic[tree[j]] -= 1
                if dic[tree[j]] == 0:
                    del dic[tree[j]]
                j += 1
            maxlen = max(maxlen, i-j+1)
        return maxlen if maxlen != -float('inf') else 0
