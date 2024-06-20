/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let M = matrix.length
    let N = matrix[0].length
    let res = []
    var inBounds = (i, j) => {
        return 0 <= i && i < M && 0 <= j && j < N
    }
    let visited = new Set()
    visited.add(`${0},${0}`)
    let i = 0
    let j = 0
    res.push(matrix[i][j])
    // while we haven't visited all cells yet
    while (visited.size < (N*M)){
        // if we can go left, continue going left
        while (inBounds(i, j+1) && !visited.has(`${i},${j+1}`)){
            visited.add(`${i},${j+1}`)
            res.push(matrix[i][j+1])
            ++j
        }
        // if we can go down, continue going down
        while (inBounds(i+1,j) && !visited.has(`${i+1},${j}`)){
            visited.add(`${i+1},${j}`)
            res.push(matrix[i+1][j])
            ++i
        }
        // if we can go right, continue going right
        while (inBounds(i, j-1) && !visited.has(`${i},${j-1}`)){
            visited.add(`${i},${j-1}`)
            res.push(matrix[i][j-1])
            --j
        }
        // if we can go up, continue going up
        while (inBounds(i-1, j) && !visited.has(`${i-1},${j}`)){
            visited.add(`${i-1},${j}`)
            res.push(matrix[i-1][j])
            --i
        }
    }
    return res
};