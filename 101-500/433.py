class Solution(object):
    def canMutation(self, w, d, c, q):
        l = ["A",'C','G','T']
        for i in range(len(w)):
            for j in l:
                if w[i] != j:
                    v = w[:i] + j + w[i + 1:]
                    if v in d and (d[v] == 0 or d[v] > c + 1):
                        d[v] = c + 1
                        q.append(v)

    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        dic = {}
        count = 0
        for i in bank:
            dic[i] = count
        queue = [start]
        while len(queue) > 0:
            q2 = []
            for i in queue:
                self.canMutation(i, dic, count, q2)
            if dic[end] != 0:
                break
            queue = q2
            q2 = []
            count += 1
        # print dic
        if dic[end] == 0:
            return -1
        return dic[end]
