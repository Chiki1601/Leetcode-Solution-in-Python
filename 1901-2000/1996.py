class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda x:(-x[0], x[1]))
        ans = 0
        max_def = 0
        for _, cur_def in properties:
            if cur_def < max_def:
                ans += 1
            else:
                max_def = cur_def
        return ans
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        
