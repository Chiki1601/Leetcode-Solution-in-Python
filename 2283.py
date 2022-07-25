class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        c = collections.Counter(num)
        for i in range(len(num)):
            if c[str(i)] == int(num[i]):
                continue
            else:
                return False
        return True
