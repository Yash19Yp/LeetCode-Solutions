# Time:  O(n^3)
# Space: O(n)

class Solution(object):
    def numberOfPaths(self, n, corridors):
        """
        :type n: int
        :type corridors: List[List[int]]
        :rtype: int
        """
        adj = [set() for _ in xrange(n)]
        for u, v in corridors:
            adj[min(u, v)-1].add(max(u, v)-1)
        return sum(sum((k in adj[i]) for j in adj[i] for k in adj[j]) for i in xrange(n))
