class Solution:
    def clearDigits(self, s):
        res = ""
        for c in s:
            if c.isdigit():
                if res:
                    res = res[:-1]  # Remove last char
            else:
                res += c  # Add char to stack
        return res
