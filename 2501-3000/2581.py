class Solution(object):
    def rootCount(self, edges, guesses, k):
        """
        :type edges: List[List[int]]
        :type guesses: List[List[int]]
        :type k: int
        :rtype: int
        """
        self.k = k
        g = set(map(tuple,guesses))
        uag = defaultdict(list)
        for a, b in edges:
            uag[a].append(b)
            uag[b].append(a)
        been = set([0])
        self.crr = 0
        def dfs(node):
            for n in uag[node]:
                if n in been:
                    continue
                been.add(n)
                self.crr += (node, n) in g
                dfs(n)
        def rev(node):
            for n in uag[node]:
                if n in been:
                    continue
                been.add(n)
                self.crr -= (node, n) in g
                self.crr += (n, node) in g
                if self.crr >= self.k:
                    self.ans += 1
                rev(n)
                self.crr -= (n, node) in g
                self.crr += (node, n) in g
        dfs(0)
        been = set([0])
        self.ans = int(self.crr >= k)
        rev(0)
        return self.ans
