/**
 * @param {number[][]} matrix
 * @return {number}
 */
var longestIncreasingPath = function(matrix) {
    /*
    Brute Force DFS:
    O(N*M*(N+M))
    2-D loop, and within each iteration, it performs DFS
    
    Optimizations?
    at each i,j, store the longest possible increasing path that can be made starting at i, j
    Since we will revisit the same cells as we perform DFS on each cell.
    
    Memoization will allow a time complexity of O(N*M) as it will only visit each cell at most one time,
    since previous results will be stored in memo object
    */
    var inBounds = function(i, j){
        return 0 <= i && i < matrix.length && 0 <= j && j < matrix[0].length
    }
    let directions = [{x: 0, y: 1}, {x: 0, y: -1}, {x: -1, y: 0}, {x: 1, y: 0}]
    
    let maxPath = Number.NEGATIVE_INFINITY
    visited = new Set()
    let memo = {}
    var dfs = function(i, j, prev){
        if (`${i},${j}` in memo){
            return memo[`${i},${j}`]
        }
        let path = 1
        for (let {x,y} of directions){
            let newX = x + i
            let newY = y + j
            // if the previous element is greater than the current, DFS down this path
            if (inBounds(newX, newY) && !visited.has(`${newX},${newY}`) && matrix[newX][newY] > prev){
                visited.add(`${newX},${newY}`)
                // on each recursive call, increment by 1 to show that we correctly visited a cell with value > prev
                path = Math.max(path, 1 + dfs(newX, newY, matrix[newX][newY]))
                // once we are done traveling the path, we delete this cell from visited
                // as another path may pass through this cell later on in the recursion
                visited.delete(`${newX},${newY}`)
            }
        }
        // in the base case, we don't continue DFS down any more grid cells,
        // so this would return 1 since the cell itself is counted as "1" on the path
        // in the case we visited a path via the for loop and we're now exiting as we've visited all paths,
        // memoize the longest path that we found from i, j
        memo[`${i},${j}`] = path
        return path
    }
    
    for (let i = 0; i < matrix.length; ++i){
        for (let j = 0; j < matrix[0].length; ++j){
            maxPath = Math.max(maxPath, dfs(i, j, matrix[i][j]))
        }
    }
    return maxPath
    
};