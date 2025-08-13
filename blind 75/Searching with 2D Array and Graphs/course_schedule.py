'''
https://leetcode.com/problems/course-schedule/
https://www.youtube.com/watch?v=EgI5nU9etnU&t=184s

Cycle Detection Algorithm using DFS
O(N+M) time, O(N) space

Create adjacency list using a dict, mapping the course as the key, and the prereqs as edges in a list
loop through all courses and run DFS on each course, keeping track of visited set
within DFS, 
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Revisited 8/12/2025
        Revisited 4/7/2025
        Revisited 10/2/2024
        https://neetcode.io/problems/course-schedule
        (Note that I found out about this via the youtube comments on the course-schedule-ii solution video)
        This can be solved in the same way as course schedule II by keeping track of two sets,
        one set is the visited set which tracks whether the courses could be fully completed, and
        tracks progress across multiple DFS calls. This is to prevent us from making the same
        recursive calls on courses that we know are valid and can be fully completed including all of its prereqs.

        The other set is the cycle set, which only checks within one DFS call of whether a course
        was already seen in this path. In that case, return False
        """
        adjacency = {}
        for i in range(numCourses):
            adjacency[i] = []
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]
            if course in adjacency:
                adjacency[course].append(prereq)
        
        cycle = set()
        visited = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for prereq in adjacency[course]:
                if (not dfs(prereq)):
                    return False
            cycle.remove(course)
            visited.add(course)
            return True
        
        for i in range(numCourses):
            if (not dfs(i)):
                return False
        return True
'''
Revisited on 7/19/2023
https://www.youtube.com/watch?v=EgI5nU9etnU&ab_channel=NeetCode

Cycle Detection
O(N+P) where N is the amount of courses and P is the amount of prerequisites for the course
Space is O(N+P) to hold all courses and prereqs in the adjacency list
Key concepts:
1) creating the adjacency list based on the prereqs, where the key is the course
and the value is the list of prereqs

when we say [2,1], this means course 1 is a prereq for course 2, so 
the graph visual would be 2 --> 1

2) Applying DFS, but keeping track of a visited set to track cycles. If at any point, we're at a given course
but it's already in the visited set, this is a cycle.

3) The base case is that a course has no prereqs, which means 
the course can be taken at any time, return True

4) After visiting all of a course's prereqs within DFS, once the recursive case goes back to the given course,
we can just remove the prereqs from the list of prereqs to avoid extra recursive calls

'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list where the key is the class
        # and the value is a list of the prereqs
        prereqMap = dict()
        for i in range(numCourses):
            prereqMap[i] = []
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]
            prereqMap[course].append(prereq)
        visited = set()
        def dfs(course: int):
            # if this course was already visited
            # this is a cycle, so course cannot be completed
            if course in visited:
                return False
            # if the course does not have prereqs, return True
            if prereqMap[course] == []:
                return True
            # add course to visited set
            visited.add(course)
            prereqs = prereqMap[course]
            for prereq in prereqs:
                # if any of the prereqs cannot be completed, return False
                if not dfs(prereq):
                    return False
            # afte visiting all prereqs for this course, 
            # remove the course from the visited set
            # and remove all prereqs to avoid iterating through them again accidentally 
            visited.remove(course)
            prereqMap[course] = []
            return True
        
        for course in prereqMap:
            if not dfs(course):
                return False
        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## the idea is basically a cycle detection algorithm using DFS
        ## if we've found a cycle, we can't complete all the courses
        ## if no cycle is found, we check if all nodes were visited in our discovered array
        adjacency_list = dict()
        for i in range(numCourses):
            adjacency_list[i] = []
        for prereq in prerequisites:
            course = prereq[0]
            prereq_course = prereq[1]
            if (adjacency_list.get(course)):
                adjacency_list[course].append(prereq_course)
            else:
                adjacency_list[course] = [prereq_course]
        
        discovered = [False] * numCourses
        in_path = [False] * numCourses
        def dfs(i):
            ## mark the current as visited
        	discovered[i] = True
	        ## mark the current node as visited in the current recursive stack that we're on
	        in_path[i] = True
	        ## for every neighbor
	   
	        for vertex in adjacency_list[i]:
	            ## if we haven't traversed further down this vertex, traverse further
	            ## however, if at any point the recursion returns False, a cycle has been found
                ## so we cannot complete all the courses
	            if (not discovered[vertex] and not dfs(vertex)):
	            	return False
	            ## in our recursion stack, if the node that we're currently on is found as
	            ## one of the adjacent neighbors, then we've hit a cycle, so return false, since we can't finish all the courses
	            elif (in_path[vertex]):
	                return False 
	        
	        ## in our backtracking, pop the current node off the current recursive stack
	        in_path[i] = False
	        return True 
        
        ## loop through each course to check for courses that don't have any prereqs, nor are prereqs for other classes
        ## (meaning its just a node by itself with no edges)
        for i in range(numCourses):
            ## if a cycle is found, the self.dfs function will return False
            if (not dfs(i)):
                return False
        ## if we're able to complete the dfs without reaching a cycle or finding a node
        ## that we cannot visit, then return True
        return True
                        
                
        
                              
                
        
                              