class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Resultant string
        result = ""
        # Indices for a and b
        aLength = len(a) - 1
        bLength = len(b) - 1
        # Carry
        carry = 0
        # Loop for all the characters in the strings
        while aLength >= 0 or bLength >= 0:
            # Sum of two bits
            totalSum = carry
            if aLength >= 0:
                totalSum += int(a[aLength])
                aLength -= 1
            if bLength >= 0:
                totalSum += int(b[bLength])
                bLength -= 1
            # Add the bit to te result
            result = str(totalSum % 2) + result
            # Modify carry
            carry = totalSum // 2
        # Final check if carry exists
        if carry > 0:
            result = str(1) + result
        return result
