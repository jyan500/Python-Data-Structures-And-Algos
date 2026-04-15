class Solution {
    /**
     * @param {number[][]} matrix
     * @return {number[][]}
     */
    transpose(matrix) {
        /*
            row 1 is converted to column 1
            row 2 is converted to column 2, etc 

            Algorithm:
            create a new 2D array where the amount of rows = amount of columns
            so a 2x3 array becomes a 3x2 array in the transposed dimension

            when iterating the original array,
            the indices are flipped so that a given i, j would transpose to j, i in the flipped version.

            For example: [[0,1,2]
                          [1,2,3]
                                 ]
            0, 1 should be 1,0
            0, 2 should be 2, 0

            [0 ...
             1 ...
             2 ...]

            Time: O(N*M)
            Space: O(N*M)

        */
        let copy = []
        // the number of cols becomes the number of rows
        // and vice versa, build the new array with the new dimensions
        let M = matrix[0].length
        let N = matrix.length
        for (let i = 0; i < M; ++i){
            let inner = []
            for (let j = 0; j < N; ++j){
                inner.push(0)
            }
            copy.push(inner)
        }
        for (let i = 0; i < matrix.length; ++i){
            for (let j = 0; j < matrix[0].length; ++j){
                // row becomes the column and vice versa, hence the j, i
                copy[j][i] = matrix[i][j]
            }
        }
        return copy
    }
}
