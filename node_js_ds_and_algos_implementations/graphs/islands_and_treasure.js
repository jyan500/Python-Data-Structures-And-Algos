/*
https://neetcode.io/problems/islands-and-treasure

Approach:
BFS and Reverse Thinking
Rather than figuring out the distance from a land cell to a treasure cell,
start from the treasure cell and work backwards towards the land cell, tracking the elapsed
distance

1) Find all cells with value === 0 (treasure chests)

2) Looping through the coords that have value 0, perform BFS starting from  
these coords. Within the Queue for the BFS, we keep track of the coordinates and also
the total elapsed distance starting from the treasure cell.

3) Also keep an object which tracks the land cells and the total elapsed distance,
later on if there's another treasure cell, we may need to update the total elapsed distance
by doing Math.min(total elapsed distance in this BFS iteration, the current dict value)

4) After the BFS is done for all treasure cells, loop through the grid and set the values
based on what was stored in the object

O(N*M) time
O(N*M) space
*/
class Solution {
    /**
     * @param {number[][]} grid
     */
    islandsAndTreasure(grid) {
        var inBounds = function(i, j){
            return i >= 0 && i < grid.length && j >= 0 && j < grid[0].length
        }
        const INF = 2**31-1
        let treasures = []
        let directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        let distanceMap = {}
        // push all cells with value === 0 onto the queue, including
        // the coordinates and the total distance traveled so far
        for (let i = 0; i < grid.length; ++i){
            for (let j = 0; j < grid[0].length; ++j){
                if (grid[i][j] === 0){
                    treasures.push({i: i, j: j})
                }
            }
        }
        for (let treasure of treasures){
            let queue = []
            queue.push({i: treasure.i, j: treasure.j, distance: 0})
            let visited = new Set()

            while (queue.length > 0){
                let {i, j, distance} = queue.shift()
                for (let d of directions){
                    let [x, y] = d
                    let newX = x + i
                    let newY = y + j
                    let coord = `${newX},${newY}`
                    if (inBounds(newX, newY) && !visited.has(coord) && grid[newX][newY] === INF){
                        visited.add(coord)
                        queue.push({i: newX, j: newY, distance: distance + 1})
                        distanceMap[coord] = coord in distanceMap ? Math.min(distanceMap[coord], distance+1) : distance+1
                    }
                }
            }

        }
        for (let i = 0; i < grid.length; ++i){
            for (let j = 0; j < grid[0].length; ++j){
                let coord = `${i},${j}`
                if (coord in distanceMap){
                    let [x,y] = coord.split(",")
                    grid[x][y] = distanceMap[coord]
                }
            }
        }
    }
}
