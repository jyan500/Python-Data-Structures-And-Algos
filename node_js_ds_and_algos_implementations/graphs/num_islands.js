/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const inBounds = (i, j, m, n) => {
        return 0 <= i && i < m && 0 <= j && j < n
    }
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    let visited = new Set()
    // perform a DFS in all four directions (up, down, left, right)
    // keep a visited set that tracks all the grid panels with value === "1"
    const dfs = (i, j, grid) => {
        for (let d of directions){
            let [x, y] = d
            let newX = i + x
            let newY = j + y
            if (inBounds(newX, newY, grid.length, grid[0].length) && !visited.has(`${newX},${newY}`) && grid[newX][newY] === "1"){
                visited.add(`${newX},${newY}`)
                dfs(newX, newY, grid)
            } 
        }
    }

    let numIslands = 0
    for (let i = 0; i < grid.length; ++i){
        for (let j = 0; j < grid[i].length; ++j){
        	// if we've already been to this grid panel with value === "1", that means
        	// we've already counted the island here, otherwise we would perform the DFS starting from
        	// this panel at i,j 
            if (grid[i][j] === "1" && !visited.has(`${i},${j}`)){
                visited.add(`${i},${j}`)
                dfs(i, j, grid)
                ++numIslands
            }
        }
    }
    return numIslands
};