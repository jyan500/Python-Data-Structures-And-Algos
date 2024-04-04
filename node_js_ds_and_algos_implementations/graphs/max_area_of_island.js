/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    let globalVisited = new Set()
    let maxArea = 0
    var inBounds = function(i, j){
        return i >= 0 && i < grid.length && j >= 0 && j < grid[0].length
    }
    var search = function(i, j, visited){
        let directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for (let d of directions){
            let [x, y] = d
            let newX = x + i
            let newY = y + j
            if (inBounds(newX, newY) && !visited.has(`${newX},${newY}`) && grid[newX][newY] === 1){
                visited.add(`${newX},${newY}`)
                search(newX, newY, visited)
            }
        }
    }
    for (let i = 0; i < grid.length; ++i){
        for (let j = 0; j < grid[0].length; j++){
            if (grid[i][j] === 1 && !globalVisited.has(`${i},${j}`)){
                let visited = new Set()
                visited.add(`${i},${j}`)
                let island = search(i, j, visited)
                maxArea = Math.max(maxArea, visited.size)
                globalVisited = new Set([...globalVisited, ...visited])
            }
        }
    }
    return maxArea
};