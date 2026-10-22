class Solution {
    /**
     * @param {number[][]} matrix
     * @return {void}
     */
    rotate(matrix) {
        /* 
        two steps:
        mirror every element to the opposite diagonal
        reverse each row

        1 2 
        3 4 
        mirror becomes
        1 3
        2 4

        reverse
        3 1
        4 2

        Note that a much simpler way to represent this is in two for loops (rather than
        the inner while loops like below)

        for (let i = 0; i < M; ++i){
            for (let j = i; j < N; ++j){
                // swap i,j with j,i
                // i = 1
            }
        }

        [1 2 3 4]
         5 [6 7 8]
         9 10 [11 12]
         13 14 15 [16]
        
        the way this works is that you do 
        0 ... N - 1, and at the same time, swap the diagonals i,j and j,i
        then 1 ... N - 1
        and so on
        */
        let M = matrix.length
        let N = matrix[0].length
        for (let i = 0; i < matrix.length; ++i){
            for (let j = i; j < N; ++j){
                // shorthand for swapping: similar to python except it's destructuring the array
                [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]
            }
        }
        for (let i = 0; i < M; ++i){
            matrix[i].reverse()
        }
    }
}

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    let N = matrix.length
    /*
    1 2 3
    4 5 6
    7 8 9
    
    1) Swap each element across its diagonal. In order to do this, we
    need to iterate across each row, but after each iteration, we start iterating
    from j = i rather than j = 0
    
    i = 0 (iterates across matrix[0][0], matrix[0][1], matrix[0][2] and performs swaps with
    matrix[1][0], matrix[2][0])
    1 2 3 
    4
    7
    
    and then
    i = 1, iterates across matrix[1][1], matrix[1][2] and performs swaps
    with matrix[2][1]
    
    5 6
    8
    
    and then
    9
    
    1 4 7
    2 5 8
    3 6 9
    
    2) Reverse each row to get the final answer
    
    7 4 1 
    8 5 2
    9 6 3
    
    */
    for (let i = 0; i < N; ++i){
        for (let j = i; j < N; ++j){
            let temp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = temp
        }
    }
    for (let i = 0; i < N; ++i){
        matrix[i].reverse()
    }
};