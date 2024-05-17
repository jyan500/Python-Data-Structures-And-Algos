/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
/*
Approach:
Using DFS, traverse in the down and right directions until the base case,
where you reach the bottom right hand corner of the grid
(i === m - 1, j === n - 1)

If (base case), return 1, since this is a valid path

store a count within each recursive call at i,j which denotes the amount of possible valid paths
that can be reached starting from i, j. The result of this is stored in a memo dict, where
the key is {i, j} to represent the current grid cell, and the value is the amount of possible
paths to the base case.

Time Complexity: O(N^2) (with memoization)
Space: O(N^2) (total amount of grids in the cell)
*/
var uniquePaths = function(m, n) {
    var inBounds = function(i, j){
        return i >= 0 && i < m && j >= 0 && j < n
    }
    let visited = new Set()
    let count = 0
    let memo = {}
    var dfs = function(i, j){
        let directions = [[0, 1], [1, 0]]
        if (i === m-1 && j === n-1){
            return 1
        }
        if (`${i},${j}` in memo){
            return memo[`${i},${j}`]
        }
        visited.add(`${i},${j}`)
        let count = 0
        for (let d of directions){
            let [x, y] = d
            let newX = i + x
            let newY = j + y
            if (inBounds(newX, newY) && !visited.has(`${newX},${newY}`)){
                count += dfs(newX, newY)
            }
        }
        memo[`${i},${j}`] = count
        visited.delete(`${i},${j}`)
        return count
    }
    return dfs(0,0)
};