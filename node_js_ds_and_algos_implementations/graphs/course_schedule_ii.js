/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    /*
    topological sort + cycle detection
    the additional visited set on the outside is to prevent us 
    from revisiting a prereq that we've already visited 

    basically as we visit all prereqs, after getting to the last prereq
    in the recursive path, we add that to the stack. And as we go back
    to previous calls, we would add those prereqs to the stack
	
	Time:	
	O(V+E), O is the amount of vertices and E is the amount of edges in the graph
    */
    let adjacency = {}
    for (let i = 0; i < numCourses; ++i){
        adjacency[i] = []
    }
    for (let pair of prerequisites){
        let [course, prereq] = pair
        adjacency[course].push(prereq)
    }
    let stack = []
    let visited = new Set()
    var dfs = function(course, cycleDetection){
        if (cycleDetection.has(course)){
            return false 
        }
        cycleDetection.add(course)
        for (let prereq of adjacency[course]){
            if (!visited.has(prereq)){             
                if (!dfs(prereq, cycleDetection)){
                    return false
                }
            }
        }
        visited.add(course)
        stack.push(course)
        cycleDetection.delete(course)
        return true
    }
    for (let i = 0; i < numCourses; ++i){
        if (!visited.has(i)){
            if (!dfs(i, new Set())){
                return []
            }
        }
    }
    return stack
};