import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        def DFS(node):
            if visited[node] == 1:
                return False
            
            visited[node] = 1
            for nbr in G[node]:
                if visited[nbr] != 2 and not DFS(nbr):
                    return False
            
            visited[node] = 2
            return True
        
        G = collections.defaultdict(list)
        for postreq, course in prerequisites:
            G[course].append(postreq)
            G[postreq]
        
        visited = [0] * numCourses
        for node in G:
            if not visited[node]:
                if not DFS(node):
                    return False
        return True
prerequisites = [[1, 0], [0, 1]]    
solution = Solution()
numCourses = 2
result = solution.canFinish(numCourses, prerequisites)
print(result)