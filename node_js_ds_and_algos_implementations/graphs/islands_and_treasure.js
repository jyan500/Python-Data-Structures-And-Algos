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
        /* 
        Revisited 8/24/2026
        My initial solution was to use BFS on each land cell.
        But the "reverse thinking" strategy which is more optimal is to
        instead place all the "chest" cells on to the queue, and then apply BFS,
        increasing the distance each time we reach a land cell, and then directly
        modifying the grid at that point. It's guaranteed to be the shortest distance
        */
        const LAND = 2**31 - 1
        const CHEST = 0
        const directions = [[0,1],[0,-1],[1,0],[-1,0]]
        const inBounds = (i, j) => {
            return 0 <= i && i < grid.length && 0 <= j && j < grid[0].length
        }

        let q = []
        // find all chest cells and add to queue
        for (let i = 0; i < grid.length; ++i){
            for (let j = 0; j < grid[0].length; ++j){
                if (grid[i][j] === CHEST){
                    q.push([i,j,0])
                }
            }
        }
        // apply BFS on each chest cell, by initially starting from each chest cell in the queue,
        // and then pushing land cells,
        // we guarantee the moment we reach a land cell, that would automatically
        // be the shortest distance to a chest cell. We can just modify the cell
        // directly as we search. This also acts as a "visited" set also since
        // it will not detect a grid cell we've already visited as a land cell since it has a number thats not INF
        while (q.length){
            let [i,j,dist] = q.shift()
            for (let [x,y] of directions){
                let newX = x+i
                let newY = y+j
                if (inBounds(newX,newY) && grid[newX][newY] === LAND){
                    grid[newX][newY] = dist + 1
                    q.push([newX,newY,dist+1])
                }
            }
        }
    }
}

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
