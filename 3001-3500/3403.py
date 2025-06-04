class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """

        # Step 1: Handle edge case
        if numFriends == 1:
            return word

        n = len(word)
        # Step 2: Max allowed length for a single part
        max_len = n - numFriends + 1
        res = ""

        # Step 3: Iterate over possible start positions
        for i in range(n):
            end = min(n, i + max_len)
            substr = word[i:end]

            # Step 4: Update result if this substring is larger
            if substr > res:
                res = substr

        # Step 5: Return the best substring
        return res
