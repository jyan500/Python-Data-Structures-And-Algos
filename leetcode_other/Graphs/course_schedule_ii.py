"""
Revisited on 8/22/2023
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = dict()
        for i in range(numCourses):
            adjacencyList[i] = []
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]
            adjacencyList[course].append(prereq)
        self.stack = []
        self.visited = set()
        self.cycleDetect = set()
        def topologicalSort(node):
            if node in self.cycleDetect:
                return False
            self.cycleDetect.add(node)
            for n in adjacencyList[node]:
                if n not in self.visited:
                    if not topologicalSort(n):
                        return False
            self.visited.add(node)
            self.stack.append(node)
            self.cycleDetect.remove(node)
            return True
        for i in range(numCourses):
            if i not in self.visited:
                if not topologicalSort(i):
                    return []
        return self.stack
        
class Solution:
    ## concept is that we want to apply topological sort, as well
    ## as make sure that our graph has no cycles

    ## within our dfs
    ## in our backtracking, remove the current node off of our in path set
    ## but also add the current node to our course stack
    ## since we've finished iterating through adjacency_list[i] at this point, through the recursive
    ## calls that occur in that for loop, we would've already added all the prereqs necessary
    ## for our current node i, so we can safely add i to the stack since all its prereqs would already
    ## be present
    ## this is essentially our topological sort

    ## Time complexity is O(V+E), where V is the number of vertices and E is the number of edges
    ## where we iterate through each vertices and each edge for the vertices only once
    ## Space complexity: O(V) vertices in our adjacency list, and O(E) to account for recursive call stack
    ## for a total of O(V+E)
    ## in the case we have a straight line graph (i.e 0:[1],2:[1], 3:[2], 4:[3]), etc
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ## create adjacency list for directed graph
        adjacency_list = dict()
        for i in range(numCourses):
            adjacency_list[i] = []
       
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]
            if (course in adjacency_list):
                adjacency_list[course].append(prereq)

        ## apply DFS, in our visited set, we can store a tuple with the node visited, along with the path taken
        path = []
        visited = set()
        in_path = set()
        course_stack = []
        
        for i in range(numCourses):   
            ## if we haven't visited this course already from our DFS, and our DFS does not find a cycle
            if (i not in visited and not self.dfs(adjacency_list, visited, in_path, i, course_stack)):
                return []
        return course_stack
            
        
    ## dfs that will traverse the graph
    def dfs(self,adjacency_list : dict, visited : set, in_path : set,i: int, course_stack: []):
        visited.add(i)
        in_path.add(i)
        for vertex in adjacency_list[i]:
                
            ## if we visit this vertex, traverse further down (self.dfs), however if it returns False
            ## that means a cycle has been found
            if vertex not in visited and not self.dfs(adjacency_list, visited, in_path,vertex, course_stack):
                return False
            ## if our vertex is in path, that means that the node we're currently on
            ## is one of the adjacent neighbors, so its a cycle
            elif vertex in in_path:
                return False
        
        course_stack.append(i)
        in_path.remove(i)
        return True
    
    '''
        test case
        inputs: 
        numCourses = 6
        prereq_list = [[0,1],[2,3],[2,4],[3,5],[4,1],[5,0]]
        
        adjacency_list = {0:[1], 1:[], 2:[3,4], 3:[5], 4:[1], 5: [0]}
        first iteration (0:[1]):
        visited = {0}
        in_path = {0}
        course_stack = []
        in_path = {0}
        dfs into 1
        
        visited = {0,1}
        in_path = {0,1}
        course_stack appends 1, [1]
        in_path removes 1 = {0}
        dfs exits
        
        course_stack appends 0, [0]
        in_path removes 0 = {}
        returns true, moves onto 1
        
        1 is already visited, skip to 2
        visited = {0,1,2}
        in_path = {2}
        
        iterate through 2's neighbors, dfs into 3
        visited = {0,1,2,3}
        in_path = {2,3}
        
        dfs into 3's neighbors (3:[5])
        visited = {0,1,2,3,5}
        in_path = {2,3,5}
        
        iterate into 3's neighbors, dfs into 5, 5:[0]
        already visited 0
        course stack adds 5 = [1,0,5]
        in path removes 5 = {2,3}
        
        backtrack into 3's neighbors, nothing left
        in_path removes 3, = {2}
        course stack adds 3, [1,0,5,3]
        
        backtrack into 2's neighbors, 4 is left
        dfs into 4 (4:[1])
        add 4 to visited {0,1,2,3,5,4}
        in path adds 4: {2,4}
        iterate through 4's neighbors, 1
        but 1 is already visited, skip
        course stack adds 4 = [1,0,5,3,4]
        in path removes 4 = {2}
        
        backtrack into 2, neighbors are done iterating
        add 2 into course stack = [1,0,5,3,4,2]
        in path removes 2 = {}
        
        go back into outer loop
        3,4,5 are already in visited so we just skip those and don't go into dfs
        
        course stack results is [1,0,5,3,4,2]
   
        
    '''
        
                
       
            
            
        