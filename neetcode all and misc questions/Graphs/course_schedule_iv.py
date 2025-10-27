"""
Time: O(N+M) (with memoization)
Space: O(N+M)

After building the adjacency list, the goal is to check given our query,
if query[0] can reach query[1] within our graph successfully?

The tricky part is the memoization aspect, because without it, we would
have many redundant DFS calls that checks whether a given node in the path can reach the target.
I structured the memoization dict so that it has subcategories, where the key is the target,
and then the subcategory is whether a given node can reach the target.

For example:
numCourses = 3
prereqs = [[1, 0], [2, 1]]
queries = [[2, 0], [1, 0]]

For example, if we check whether 2 can reach 0:
we see that the path taken is 2 -> 1 -> 0. 

The memoization dict would be {0: {2: true, 1: true}}
If we were to perform the 2nd query, 1 -> 0,
we can first reference the target 0 inside the dict,
{2: true, 1: true}, and see that 1 already exists and we've proven that
1 can go to 0. So we can just return true right away without needing to perform DFS any further.
This way, it avoids many redundant calls.


"""
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjacency = {}
        for i in range(numCourses):
            adjacency[i] = []
        for course, prereq in prerequisites:
            adjacency[course].append(prereq)
        # within the query, we check given query[0], can we successfully
        # traverse the graph to query[1] using DFS?
        # is there a way to memoize results?
        # the memoize dict here will track per target, a separate dict,
        # that tracks whether a given node can reach the target
        # if we've already seen that a given node can reach the target, we can just
        # return the stored result
        res = []
        memoize = {}
        def dfs(node, target):
            if node in memoize[target]:
                return memoize[target][node]
            if node == target:
                return True
            for neighbor in adjacency[node]:
                memoize[target][neighbor] = dfs(neighbor, target)
                if memoize[target][neighbor]:
                    return True
            memoize[target][node] = False
            return False
        
        for course, target in queries:
            if target not in memoize:
                memoize[target] = {}
            res.append(dfs(course, target))
        return res