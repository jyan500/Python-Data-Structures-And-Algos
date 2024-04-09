/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    /* 
    BFS, since we want to see the results of the rotting in intervals (rather than using DFS, which would only show the rotting down
    one specific "path")

	Time:
    O(N*M + N+M) (for the BFS and grid traversal)
    Space:
    O(N*M) for visited
    */
    var inBounds = function(i,j){
        return i >= 0 && i < grid.length && j >= 0 && j < grid[0].length
    }
    // push all rotten oranges onto the queue, this includes the (i, j) as well as the minutes
    let queue = []
    let directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    let visited = new Set()
    for (let i = 0; i < grid.length; ++i){
        for (let j = 0; j < grid[0].length; ++j){
            if (grid[i][j] === 2){
                queue.push({i, j, minutes: 0})
            }
        }
    }

    /* 
    applying BFS, check if at any point we can visit the orange directly to the left, up, right or down direction
    making sure that it's not in the visited set already, and that it's a fresh orange with value === 1
    
    if so, push the orange onto the queue, also set the grid value to be 2 to show that it's rotten
    also increment the minutes variable as we push onto the queue to show that at this point on the queue,
    this is how much time has elapsed.
    
    */
    let minMinutes = 0
    while (queue.length > 0){
        let {i, j, minutes} = queue.shift()
        for (let d of directions){
            let [x, y] = d
            let newX = x + i
            let newY = y + j
            if (inBounds(newX, newY) && !visited.has(`${newX},${newY}`) && grid[newX][newY] === 1) {
                visited.add(`${newX},${newY}`)
                grid[newX][newY] = 2

                queue.push({i: newX, j: newY, minutes: minutes + 1})
                minMinutes = minutes + 1
            }
        }
    }
    
    // if there's still any oranges that are fresh, that means the rotting wasn't able to reach all oranges, 
    // so return -1
    for (let i = 0; i < grid.length; ++i){
        for (let j = 0; j < grid[0].length; ++j){
            if (grid[i][j] === 1){
                return -1
            }
        }
    }
    return minMinutes
    
};