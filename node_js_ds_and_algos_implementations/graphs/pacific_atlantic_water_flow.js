/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    let res = []
    var inBounds = function(i, j){
        return 0 <= i && i < heights.length && 0 <= j && j < heights[0].length
    }
    var isPacific = function(i, j){
        return i === 0 || j === 0
    }
    var isAtlantic = function(i, j){
        return i === heights.length - 1 || j === heights[0].length - 1
    }
    var search = function(i, j, visited, result){
        if (isPacific(i, j)){
            result[0] = true
        }
        if (isAtlantic(i, j)){
            result[1] = true
        }

        let directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for (let d of directions){
            let [x,y] = d
            let newX = x + i
            let newY = y + j
            if (inBounds(newX, newY) && heights[newX][newY] <= heights[i][j] && !visited.has(`${newX},${newY}`)){
                visited.add(`${newX},${newY}`)
                if (search(newX, newY, visited, result)){
                    return true
                }
                
            }
        }
        return result[0] && result[1]
    }
    for (let i = 0; i < heights.length; ++i){
        for (let j = 0; j < heights[0].length; ++j){
            let visited = new Set()
            visited.add(`${i},${j}`)
            if (search(i, j, visited, [false, false])){
                res.push([i,j])
            }
            
        }
    }
    return res
};