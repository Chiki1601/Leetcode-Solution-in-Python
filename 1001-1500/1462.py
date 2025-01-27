class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Initialize the relation matrix
        relation = [[False] * numCourses for _ in range(numCourses)]

        # Fill in the direct prerequisites
        for d in prerequisites:
            relation[d[0]][d[1]] = True

        # Perform Floyd-Warshall-like transitive closure
        for i in range(numCourses):
            for src in range(numCourses):
                for target in range(numCourses):
                    relation[src][target] = relation[src][target] or (relation[src][i] and relation[i][target])

        # Answer the queries
        ans = []
        for d in queries:
            ans.append(relation[d[0]][d[1]])

        return ans
