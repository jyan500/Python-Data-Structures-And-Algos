class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        adjacency list relationship problem
        for the town judge property, node A points to node B (judge is node B), and node B points to nothing else
        We just have to find the single node that has no outward edges.
        There can only be one node B that points to nothing else
        If the graph is strongly connected (meaning every node points to each other and there are no nodes that have an empty adjacency list), return -1

        Also check that each node points directly at the judge:
        node A points directly at node B, cannot do node A -> middle node -> node B
        
        O(N) Time
        O(N) Space
        """
        adjacency = {}
        for i in range(n):
            adjacency[i+1] = set()
        for a, b in trust:
            adjacency[a].add(b)
        # find the judge
        # if there was more than one node that has an empty list (meaning no neighbors),
        # return False as there can only be one judge
        judge = 0
        for key in adjacency:
            if len(adjacency[key]) == 0:
                # if we already saw a judge, judge would no longer be 0 (assuming judges cannot have the value 0),
                # so this is invalid, as there's more than one judge in the town
                if judge == 0:
                    judge = key
                    break
                return -1
        # check that each node points directly to the judge (excluding the judge himself)
        for key in adjacency:
            if key != judge and judge not in adjacency[key]:
                return -1
        return judge
            