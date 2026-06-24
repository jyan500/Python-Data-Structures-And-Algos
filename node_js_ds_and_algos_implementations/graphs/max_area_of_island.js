class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        /*
        DFS to count the islands 
        keep a global visited set to avoid revisiting 
        track the amount of cells visited in the island, and take the max between the res and this amount

        time: O(M*N)
        space: O(M*N)
        */
        const directions = [[0,1],[0,-1],[1,0],[-1,0]]
        const inBounds = (i,j) => {
            return 0 <= i && i < grid.length && 0 <= j && j < grid[0].length
        }
        let visited = new Set()
        const dfs = (i, j, currentVisited) => {
            for (let [x,y] of directions){
                let newX = x+i
                let newY = y+j
                if (inBounds(newX,newY) && !visited.has(`${newX},${newY}`) && grid[newX][newY] === 1){
                    visited.add(`${newX},${newY}`)
                    currentVisited.add(`${newX},${newY}`)
                    dfs(newX,newY, currentVisited)
                }
            }
        }
        let maxIsland = 0
        for (let i = 0; i < grid.length; ++i){
            for (let j = 0; j < grid[0].length; ++j){
                if (grid[i][j] === 1 && !visited.has(`${i},${j}`)){
                    let currentVisited = new Set()
                    currentVisited.add(`${i},${j}`)
                    dfs(i,j,currentVisited)
                    maxIsland = Math.max(currentVisited.size, maxIsland)
                }
            }
        }
        return maxIsland
    }
}
