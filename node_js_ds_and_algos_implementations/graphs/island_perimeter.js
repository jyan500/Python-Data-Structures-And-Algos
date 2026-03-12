class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    islandPerimeter(grid) {
        /*
        because there is only one island, we can just assume
        that every grid[i][j] === 1 is connected to each other,
        so we don't need DFS

        in terms of the perimeter, for each cell, we need to know whether
        its on the boundaries of the grid, and/or if there's a cell === 0
        that's 4 directional to it. In that case, we would add 1 for each side
        that's either on a boundary of the grid or a water cell.
    
        O(N*M) time
        O(1) space
        */
        let total = 0
        let directions = [[0,1],[0,-1],[1,0],[-1,0]]
        function inBounds(i,j){
            return 0 <= i && i < grid.length && 0 <= j && j < grid[0].length
        }
        for (let i = 0; i < grid.length; ++i){
            for (let j = 0; j < grid[0].length; ++j){
                if (grid[i][j] === 1){
                    for (let [x,y] of directions){
                        let newX = x+i
                        let newY = y+j
                        // if the neighboring cell is out of bounds,
                        // this boundary is included in the perimeter
                        if (!inBounds(newX,newY)){
                            ++total
                        }
                        // if neighboring cell is a water cell,
                        // boundary is included in the perimeter
                        else if (inBounds(newX, newY) && grid[newX][newY] === 0){
                            ++total
                        }
                    }
                }
            }
        }
        return total
    }
}
