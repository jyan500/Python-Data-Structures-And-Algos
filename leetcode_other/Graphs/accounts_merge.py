"""
https://leetcode.com/problems/accounts-merge/
Key Concepts:
1) Identifying that this a graph problem, specifically finding connected components in an undirected graph
A connected component will represent one account, where one email in the connected component should be able to reach
the other components

2) Performing DFS to find connected components (union find also works but the solution below uses DFS),
if we're able to visit all emails starting from a given email, this is a connected component so we can merge the account,
sorting and adding all the emails we've visited into the result
We keep track of a global visited set to make sure we don't double count any nodes we've already visited

Time complexity:
O(N*K*NLogN), where N is the number of accounts, and K is the number of emails within the account,
creating the adjacency list itself is already N * K, and the sorting after the DFS multiplies this by another
NLogN

Space complexity:
O(N*K) for the adjacency list

"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # concept: find connected components
        # create adjacency list representing an undirected graph
        adjacencyList = dict()
        namesDict = dict()
        for i in range(len(accounts)):
            name = accounts[i][0]
            emails = accounts[i][1:]
            for j in range(len(emails)):
                if emails[j] in adjacencyList:
                    namesDict[emails[j]] = name
                    # every other element in this email list 
                    # is a neighbor except j itself
                    adjacencyList[emails[j]].extend(emails[:j] + emails[j+1:])
                else:
                    adjacencyList[emails[j]] = emails[:j] + emails[j+1:]
                    namesDict[emails[j]] = name
            
        visited = set()
        res = []
        def dfs(node, newVisited, visitedName):
            if node not in visited:
                visited.add(node)
                visitedName = namesDict[node]
                newVisited.append(node)
            for neighbor in adjacencyList[node]:
                if neighbor not in visited:
                    dfs(neighbor, newVisited, visitedName)
            return newVisited, visitedName
        
        for email in adjacencyList:
            newVisited, visitedName = dfs(email, [], "")
            # if we were able to visit all emails starting from this email,
            # this is a connected component, which means the account can be merged
            if len(newVisited) > 0:
                res.append([visitedName] + sorted(newVisited))
        
        return res