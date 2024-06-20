/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */

/*
Approach:
1) The trick to this problem is for each left, right, up and down direction,
if you see a "0", you iterate through each direction while in bounds,
and set each i, j that SHOULD be converted to a "0" to a "sentinel" value instead. This way, when you continue to iterate
through the rest of the 2D array, you can tell which values you'll need to 
set to zero later (and weren't zeroes originally)

1 1 1     1 * 1    1 0 1 
1 0 1  -> * 0 * -> 0 0 0 
1 1 1     1 * 1    1 0 1 

you'd convert the surrounding values around 0 to be a sentinel value, that way,
if you continue to iterate (say for position 2, 1), you'd know that this is GOING
to be set to 0, but was not originally 0, so you wouldn't apply the logic to set the surrounding elements
to zero for this particular element. This allows us to use O(1) space without needing a hashmap

Time Complexity: O(N*M)
Space: O(1)

*/
var setZeroes = function(matrix) {
    var inBounds = (i, j) => {
        return 0 <= i && i < matrix.length && 0 <= j && j < matrix[0].length
    }
    let directions = [{x: 0, y: 1}, {x: 1, y: 0}, {x: 0, y:-1}, {x: -1, y: 0}]
    for (let i = 0; i < matrix.length; ++i){
        for (let j = 0; j < matrix[0].length; ++j){
            if (matrix[i][j] === 0){
                for (let {x,y} of directions){
                    let m = i
                    let n = j
                    while (inBounds(m+x, n+y)){
                        if (matrix[m+x][n+y] !== 0){
                            matrix[m+x][n+y] = "*"
                        }
                        m += x
                        n += y
                    }
                }
            }
        }
    }
    for (let i = 0; i < matrix.length; ++i){
        for (let j = 0; j < matrix[0].length; ++j){
            if (matrix[i][j] === "*"){
                matrix[i][j] = 0
            }
        }
    }
};