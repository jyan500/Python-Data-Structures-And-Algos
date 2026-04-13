class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    minPathSum(grid) {
        /*
        1 2 0
        3 1 6
        0 0 0

        it's not a greedy approach, as picking the smallest
        number initially does not actually yield the right answer.

        Can use BFS and keep a global min, but also keep track of the current sum
        of the path inside an object in the queue

        To avoid calculating redundant paths, use a 2-D DP array,
        where you initially set all the indices as Positive Infinity, then
        as you perform BFS, you update the sum at the proposed cell that you're going
        to visit IF it makes the sum smaller

        For example, if you had two separate items on the queue, the first 
        one visits (i,j) and it results in a smaller sum, however the 2nd item gets popped off,
        it has a sum that's greater than what's in dp[i][j], so we don't continue the path
        for this one.

        Time: O(N*M)
        Space: O(N*M)

        */
        let q = []
        q.push([0,0,grid[0][0]])
        let min = Number.POSITIVE_INFINITY
        let directions = [[0,1],[1,0]]
        const inBounds = (x, y) => {
            return 0 <= x && x < grid.length && 0 <= y && y < grid[0].length
        }
        let dp = []
        for (let i = 0; i < grid.length; ++i){
            let temp = []
            for (let j = 0; j < grid[0].length; ++j){
                temp.push(Number.POSITIVE_INFINITY)
            }
            dp.push(temp)
        }
        dp[0][0] = grid[0][0]
        // to optimize the BFS approach, use DP array
        // keep track of a 2D array where on each cell, it keeps track of the min
        // sum that was found, and only push a cell onto the queue if it improves
        // the min sum for that potential cell
        while (q.length){
            let [i,j,sum] = q.shift()
            // optimization: if the current sum is greater than the dp[i][j], we don't need
            // to continue the path, dp[i][j] is the min possible sum found at this point
            if (sum > dp[i][j]){
                continue
            }
            for (let [x,y] of directions){
                let newX = x+i
                let newY = y+j
                if (inBounds(newX, newY)){
                    let newSum = sum + grid[newX][newY]
                    if (newSum < dp[newX][newY]){
                        dp[newX][newY] = newSum
                        q.push([newX, newY, sum+grid[newX][newY]])
                    }
                }
            }
        }
        return dp[grid.length-1][grid[0].length-1]
    }
}
