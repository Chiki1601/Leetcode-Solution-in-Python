import heapq

class Solution:
    def dijkstra(self, src, target, adj, n):
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == target:
                return d
            for v, w in adj[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        return INF

    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        l, h = 0, int(1e9)
        best = -1
        while l <= h:
            mid = (l + h) // 2
            adj = [[] for _ in range(n)]
            for u, v, c in edges:
                if c >= mid and online[u] and online[v]:
                    adj[u].append((v, c))
            dist = self.dijkstra(0, n - 1, adj, n)
            if dist <= k:
                best = mid
                l = mid + 1
            else:
                h = mid - 1
        return best
