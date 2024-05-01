class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        Topological Sort
        1) Build an adjacency list based on the prefix chars
        of each word
        2) Perform DFS using visit dictionary, see course schedule II for a similar solution
		https://neetcode.io/problems/foreign-dictionary
        """
        adj = dict()
        for w in words:
            for c in w:
                adj[c] = set()
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            # compare the length of the words
            minLen = min(len(w1), len(w2))
            """
            if the prefix of the two words is the same, but the 
            length of the first word in the list is bigger than the second,
            that means this is an invalid ordering of the words.

            i.e [abcd, abc], the min length is 3, so looking at the prefix "abc",
            abcd is not less than abc, so this is an invalid ordering
            """ 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            """
            find the first differing character between the two words.
            once found, add the character from w1 as the key to the adjacency list,
            and add the differing char from w2 to the set to indicate that w1[j] 
            comes before w2[j]
            Also break the loop since it's not necessary to iterate any further
            """
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        # false = visited, true = visited and in the current path
        # if visit[c] is true, there's a cycle in the graph
        res = []
        visit = dict()
        # topological sort portion
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True
            visit[c] = False
            res.append(c)
        for c in adj:
            # if there's a cycle, this is not a valid ordering configuration
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
        