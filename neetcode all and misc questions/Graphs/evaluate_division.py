class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Neetcode:
        https://youtu.be/Uei1fwDoyKk

        Explanation of the input:
        equations = [[a,b],[b,c]] values = [2,3]
        queries = [[a,c], [b,a], [a, e], [a, a], [x, x]]
        
        in the first query:
        this means that a/b = 2 and b/c = 3, 
        so [a,c] can be found by a/b * b/c = a/c, which is 6
        
        in the second query:
        a/b = 2, so b/a must be 1/2

        third query cannot be found because there's no other equation that involves "e"
        
        fourth query:
        a/b = 2, we know b/a = 1/2, so a/b * b/a = a/a, which is 1
        
        fifth query cannot be found because there's no other equation that involves "x"
        ---------------------------------------
        The key is recognizing that the numerators and denominators can be represented 
        by an adjacency list
        
        a -> b is an edge, b -> c is also an edge
        
        b -> a is also an edge, c -> b is also an edge
        
        however, it's a directed graph where the backwards edge would be the "inverse" relationship, meaning if a / b = 2, the backwards edge (b/a) is 1/2, so we'd have to represent that in the adjacency list
        
        To solve the problem once we have the adjacency list, for each query in the query list, we run BFS from query[0] and see if we can reach query[1], i.e
           2   3    
           ->  ->
        a     b    c
           <-   <-
           1/2   1/3 
           
        for example for the query ["a", "c"], we start running BFS at "a"
        a goes to b, which is 2
        and then b goes to c, which is 3. At each point, we would likely keep the current value, and at each neighbor, multiply the value to get the cumulative value as we continue BFS
        since we've reached c, we get 2 * 3 = 6, which is the correct output
        
        for the query ["b", "a"], we start at node b and see if we can reach "a",
        since "b" has two neighbors, we can go to the right to "c", but that's not the right value, so we go left instead to "a", and get 1/2
        
        for the query ["a", "e"], we run BFS starting at a, but after fully exploring 
        every edge, we see that "e" is unreachable in our graph because that node doesn't exist, so return -1
        
        Time Complexity: O(N*(E+V)), since for each query in N, we run BFS
        Space: O(E+V) to construct the adjacency
        """
        """
        adjacency format based on the example above:
        you can see the backwards edges having the inverse value
        {
            "a": [("b", 2)],
            "b": [("a", 1/2), ("c", 3)],
            "c": [("b", 1/3)]
        }
        """
        adjacency = {}
        # note that the problem constraint says len(equations) == len(values)
        for i in range(len(equations)):
            num, denom = equations[i]
            if num not in adjacency:
                adjacency[num] = []
            if denom not in adjacency:
                adjacency[denom] = []
            adjacency[num].append((denom, values[i]))
            # store the backwards relationship as the inverse
            adjacency[denom].append((num, 1/values[i]))
        
        def bfs(node, target):
            visited = set()
            q = deque([(node, 1)])
            while (q):
                num, currentVal = q.popleft()
                if num == target:
                    return currentVal
                for neighbor, weight in adjacency[num]:
                    if (neighbor, weight) not in visited:
                        visited.add((neighbor, weight))
                        q.append((neighbor, weight * currentVal))
            return -1                        
 
        res = [-1] * len(queries)
        for i in range(len(queries)):
            num, denom = queries[i]
            # currentVal initially is 1 since we're going to be multiplying numbers together
            # check if the numerator and denominator are in the adjacency, otherwise we can save some time by returning -1 since it'll be unreachable otherwise
            if num in adjacency and denom in adjacency:
                res[i] = bfs(num, denom)
            else:
                res[i] = -1
        return res
            
            
            
            
            
        
        