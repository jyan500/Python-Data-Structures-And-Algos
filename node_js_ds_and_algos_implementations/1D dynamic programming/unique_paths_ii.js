class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    uniquePathsWithObstacles(grid) {
        /*
        Apply DFS within the 2-D grid.

        can travel only down or right directions
        (1, 0) = down (0, 1) = right 

        Note that because of this rule, you actually don't need a visited set, since it's not possible
        to get stuck in a loop since we're only going right or down, and never left or upwards. If we did keep
        a visited set, we'd just have to pop out of it, since we'd likely revisit the same square multiple times.

        because there is a chance we land on the same square multiple times,
        we need to consider how many paths to the end
        are possible starting from that square.
        And then memoize it so we already know the amount of paths possible
        and don't need to recalculate it if we re-land on the square

        Time: O(N*M)
        Space: O(N*M)
        */

        if (grid[0][0] === 1){
            return 0
        }
        const M = grid.length
        const N = grid[0].length
        const directions = [[0, 1], [1, 0]]
        let memo = {}

        function inBounds(i,j){
            return i >= 0 && i < M && j >= 0 && j < N
        }

        function dfs(i,j){
            let paths = 0
            if (i === M - 1 && j === N-1){
                paths += 1
            }
            if (`${i},${j}` in memo){
                return memo[`${i},${j}`]
            }
            for (let [x, y] of directions){
                let newX = x + i
                let newY = y + j
                let coord = `${newX},${newY}`
                // if not an obstacle, and inBounds, visit
                if (inBounds(newX, newY) && grid[newX][newY] !== 1){
                    paths += dfs(newX, newY)
               
                }        
            }
            memo[`${i},${j}`] = paths
            return paths
        }

        return dfs(0,0)
    }
}
