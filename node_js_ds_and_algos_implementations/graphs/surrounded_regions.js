/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    // find all O's that are on the border of the grid,
    // and perform DFS to change these to the placeholder "T"
    var inBounds = function(i, j){
        return i >= 0 && i < board.length && j >= 0 && j < board[0].length
    }
    var dfs = function(i, j) {
        let directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        // change the current "O" to a placeholder of "T"
        board[i][j] = "T"
        for (let d of directions){
            let [x, y] = d
            let newX = i + x
            let newY = y + j
            if (inBounds(newX, newY) && board[newX][newY] === "O"){
               dfs(newX, newY) 
            }
        }
    }
    for (let i = 0; i < board.length; ++i){
        // looking at the top or bottom rows
        if (i === 0 || i === board.length - 1){
            for (let j = 0; j < board[0].length; ++j){
                if (board[i][j] === "O"){
                    dfs(i, j)
                }
            }
        }
        else {
            // left most column
            if (board[i][0] === "O"){
                dfs(i, 0)
            }
            // right most column
            if (board[i][board[0].length-1] === "O"){
                dfs(i, board[0].length-1)
            }
        }
    }
    // find any remaining O's and change to X's
    for (let i = 0; i < board.length; ++i){
        for (let j = 0; j < board[0].length; ++j){
            if (board[i][j] === "O"){
                board[i][j] = "X"
            }
        }
    }
    // change any remaining T's back to O's, since these are the ones that couldn't be flipped
    for (let i = 0; i < board.length; ++i){
        for (let j = 0; j < board[0].length; ++j){
            if (board[i][j] === "T"){
                board[i][j] = "O"
            }
        }
    }
};