class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses, prerequisites) {
        /* 
        slightly different version that uses two sets, one a global set
        which tracks whether we've seen a node already, and a per-path cycle set which
        adds and then removes it so other paths can potentially visit this node, 
        but if the same course is visited within the path, it gets marked as a cycle.
        The global visited set avoids repeated work, because if a node has already been seen,
        we already know it's not a cycle
        */
        let adjacency = {}
        for (let i = 0; i < numCourses; ++i){
            adjacency[i] = new Set()
        }
        for (let [course, prereq] of prerequisites){
            adjacency[course].add(prereq)
        }

        let cycles = new Set()
        let visited = new Set()
        const dfs = (node) => {
            // if the current path re-visits the same node, this is a cycle
            if (cycles.has(node)){
                return false
            }
            // keep track of a global visited set that confirms that we've 
            // already seen this node in a separate path, and if we haven't
            // returned false above, that means it's not a cycle so we don't need to redo
            if (visited.has(node)){
                return true
            }
            visited.add(node)
            cycles.add(node)
            for (let neighbor of adjacency[node]){
                if (!dfs(neighbor)){
                    return false
                }
            }
            // since this is a per-path visited set, we have to pop out
            // so that other courses that may have this current course as a 
            // prereq don't get excluded
            cycles.delete(node)
            return true
        }
        // need to iterate through all courses to account for disconnected components
        for (let i = 0; i < numCourses; ++i){
            if (!visited.has(i) && !dfs(i)){
                return false
            }
        }
        return true
    }
}

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    /* Create the adjacency list */
    let adjacencyList = {}
    for (let i = 0; i < numCourses; ++i){
        adjacencyList[i] = []
    }
    for (let pair of prerequisites){
        let [course, prereq] = pair
        adjacencyList[course].push(prereq)
    }
    let visited = new Set()
    /* 
        Cycle Detection using DFS
        we want to see if we accidentally a prereq is a prereq of itself,
        which would mean it's already been visited. Seeing that the adjacency list
        should represent a directed graph, the presence of the same course in visited
        would indicate that this is a cyclical.      
    */
    const canComplete = (course) => {
        if (visited.has(course)){
            return false
        }
        // if course does not have prereqs, return true
        if (adjacencyList[course].length === 0){
            return true
        }
        visited.add(course)
        for (let prereq of adjacencyList[course]){
            if (!canComplete(prereq)){
                return false
            }
        }
        // after visiting all prereqs for this course, 
        // remove the course from the visited set
        // and remove all prereqs to avoid iterating through them again accidentally 
        visited.delete(course)
        adjacencyList[course] = []
        return true
    }
    let courses = Object.keys(adjacencyList)
    for (let course of courses){
        if (!canComplete(course)){
            return false
        }
    }
    return true
};