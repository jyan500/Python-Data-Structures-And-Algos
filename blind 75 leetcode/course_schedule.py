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
                        
                
        
                              
                
        
                              