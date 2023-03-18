class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        s="aeiou"
        cnt=0
        for i in range(left,right+1):
            if words[i][0] in s and words[i][-1] in s:cnt+=1
        return cnt
