/**
 * @param {number[][]} grid
 * @return {number}
 */
/*
Time Complexity:
O(N^2LogN)
N^2 to iterate the entire 2-D array, and LogN per each iteration when popping out of the min heap
Space:
O(N^2)

The trick to this problem is recognizing that it uses BFS + Min Heap, and that the
we're keeping track of the max elevation as we iterate, this indicates the amount of time needed
to get to a given cell, so if we see another cell that has less elevation, we don't update the elevation.
*/
var swimInWater = function(grid) {
    let directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    let visited = new Set()
    var inBounds = function(x, y, grid){
        return x >= 0 && x < grid.length && y >= 0 && y < grid[0].length
    }
    let minHeap = new MinPriorityQueue({priority: (element) => element[0]})
    minHeap.enqueue([grid[0][0], [0, 0]])
    visited.add(`0,0`)
    while (!minHeap.isEmpty()){
        let [elevation, coord] = minHeap.dequeue().element
        let [i, j] = coord
        if (i === grid.length - 1 && j === grid[0].length - 1){
            return elevation
        }
        for (let [x, y] of directions){
            let newX = i + x
            let newY = y + j
            if (inBounds(newX, newY, grid) && !visited.has(`${newX},${newY}`)){
                // take the max between the elevation we're currently at, and the elevation
                // of the next elevation point we're traveling to. The min heap will pick
                // the minimal elevation that we need to travel to the next point.
                let newElevation = Math.max(elevation, grid[newX][newY])
                visited.add(`${newX},${newY}`)
                minHeap.enqueue([newElevation, [newX, newY]])
            }
        }
    }
    return -1
};