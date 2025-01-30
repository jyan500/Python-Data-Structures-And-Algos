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

# Revisited on 1/3/2025
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        represent as a graph where the emails are the nodes and the edges

        index 0: [johnsmith@mail.com, john_newyork@mail.com],
        index 1: [johnsmith@mail.com, john00@mail.com]
        index 2: [mary@mail.com]
        index 3: [johnnybravo@mail.com]

        each email within the account array is paired with each other as an edge, so if another account shares
        the same email, that would also be an edge

        john_newyork@mail.com : [johnsmith@mail.com],
        johnsmith@mail.com: [john_newyork@mail.com, john00@mail.com],
        johnnybravo@mail.com: []
        mary@mail.com: [],

        Perform DFS on the emails to check for the connected component

        """
        from collections import defaultdict
        adj = defaultdict(set)
        emailsToNames = defaultdict(str)
        # also map emails to name once the connected
        # components are found to tie the emails to a name
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for i in range(len(emails)):
                emailsToNames[emails[i]] = name
                root = emails[i]
                neighbors = emails[:i] + emails[i+1:]
                if root not in adj:
                    adj[root] = set()
                for nei in neighbors:
                    adj[root].add(nei)
        def dfs(node, graph, connected, visited):
            if node in connected:
                return
            visited.add(node)
            connected.add(node)
            for neighbor in graph[node]:
                dfs(neighbor, graph, connected, visited)
        
        visited = set()
        mergedAccounts = []
        for key in adj:
            # to avoid processing the same connected components,
            # keep global visited list
            if key not in visited:
                connected = set()
                dfs(key, adj, connected, visited)
                mergedAccount = list(connected)
                # taking the first email in the list of connected emails and mapping
                # to the name should be a safe assumption to make, since all the 
                # emails in the connected component should be tied to the same name
                # according to the problem statement.
                mergedAccounts.append([emailsToNames[mergedAccount[0]]] + sorted(mergedAccount))
        return mergedAccounts

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