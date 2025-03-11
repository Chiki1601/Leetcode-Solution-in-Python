class Solution(object):
    def numberOfSubstrings(self, s):
        count = [0] * 3  # To store counts of 'a', 'b', and 'c'
        left = 0  # Left pointer of the window
        result = 0  # To store the result

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1  # Increment the count of the current character

            # When all three characters are present in the window
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                result += len(s) - i  # All substrings starting at left and ending at i or beyond are valid
                count[ord(s[left]) - ord('a')] -= 1  # Decrement the count of the left character
                left += 1  # Move the left pointer

        return result
