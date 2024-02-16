class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        mp = {}
        for x in arr:
            mp[x] = mp.get(x, 0) + 1

        elements = sorted(mp.items(), key=lambda x: x[1])

        for key, value in elements:
            if value <= k:
                k -= value
                del mp[key]
            else:
                break
        return len(mp)
