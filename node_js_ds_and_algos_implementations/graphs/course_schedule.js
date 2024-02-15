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