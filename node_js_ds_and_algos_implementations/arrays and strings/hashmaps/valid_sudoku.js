/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const printMatrix = (b, m, n) => {
        for (let i = 0; i < m; ++i){
            console.log(board[i].join(" "))
        }
    }
    /*
    Optimized
    Create a "virtual" 3x3 grid, and convert the 9x9 indices when looping through the grid
    to their 3x3 counterpart by doing i/3 and j/3, the goal of this is that
    we want to keep track of a hashmap for each quadrant, so when doing i/3, j/3, we then 
    check whether the value is in the hashmap for that quadrant
    i.e
    0, 0 0,1 0, 2
    1,0  1,1 1, 2
    2, 0 2,1  2, 2  
    */
    let rows = {}
    let cols = {}
    let subGrids = {}
    for (let i = 0; i < 9; ++i){
        rows[i] = new Set()
    }
    for (let j = 0; j < 9; ++j){
        cols[j] = new Set()
    }
    for (let i = 0; i < 3; ++i){
        for (let j = 0; j < 3; ++j){
            subGrids[`${i},${j}`] = new Set()
        }
    }

    
    for (let i = 0; i < 9; ++i){
        for (let j = 0; j < 9; j++){
            let h = Math.floor(i/3).toString()
            let k = Math.floor(j/3).toString()
            if (rows[i].has(board[i][j])){
                return false
            }
            if (cols[i].has(board[j][i])){
                return false
            }
            if (subGrids[`${h},${k}`].has(board[i][j])){
                return false
            }
            if (board[i][j] !== "."){
                rows[i].add(board[i][j])
                subGrids[`${h},${k}`].add(board[i][j])
            }
            if (board[j][i] !== "."){
                cols[i].add(board[j][i])
            }
        }
    }
    return true
};

/**
 * @param {character[][]} board
 * @return {boolean}
 */

/* Brute Force Solution */
var isValidSudoku = function(board) {
    const printMatrix = (b, m, n) => {
        for (let i = 0; i < m; ++i){
            console.log(board[i].join(" "))
        }
    }
    // printMatrix(board, board.length, board[0].length)
    let digits = new Set()
    for (let i = 0; i < 9; ++i){
        digits.add((i+1).toString())
    }
    let rows = {}
    let cols = {}
    m = board.length
    n = board[0].length
    // check if all rows are valid
    for (let i = 0; i < m; ++i){
        for (let j = 0; j < n; ++j){
            // only consider board spots that are numbers 1 - 9
            if (digits.has(board[i][j])){
                if (board[i][j] in rows){
                    return false
                }
                else {
                    rows[board[i][j]] = 1
                }
            }
            if (digits.has(board[j][i])){
                if (board[j][i] in cols){
                    return false
                }
                else {
                    cols[board[j][i]] = 1
                }
            }
        }
        rows = {}
        cols = {}
    }
    // check 3 x 3 squares
    /*
    starting from the first quadrant and going downwards by column
        
    X                 X                  X
    X followed by ... X  followed by ... X
    X                 X                  X
    
    this is the bottle neck, O(K * (M*N)), where K is 3
    
    starts from (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2, 0),(2,1), (2,2)...
    then
    (3,0), ....
    then
    (6,0), (6,1), ...
    
    the second set of loops does 0-2
    (0,3),(0,4), (0,5)
    (1,3), (1,4), (1,5)
    (2,3), (2,4), (2,5)
    
    then 3-5
    
    (3,3),(3,4),3,5)...
    
    then 6 - 8
    
    (6,3), (6,4) ...
   
    
    */

    let factors = [0, 3, 6]
    for (let k of factors){      
        let grids = {}
        for (let i = k; i < 3+k; ++i){
            for (let j = 0; j < 3; ++j){
                if (digits.has(board[i][j])){
                    if (board[i][j] in grids){
                        return false
                    }
                    else {
                        grids[board[i][j]] = 1
                    }
                }
            }
        }
    }
    for (let k of factors){
        let grids = {}
        for (let i = k; i < 3+k; ++i){
            for (let j = 3; j < 6; j++){
                if (digits.has(board[i][j])){
                    if (board[i][j] in grids){
                        return false
                    }
                    else {
                        grids[board[i][j]] = 1
                    }
                }
            }
        }
    }
    for (let k of factors){
        let grids = {}
        for (let i = k; i < 3+k; ++i){
            for (let j = 6; j < 9; j++){
                if (digits.has(board[i][j])){
                    if (board[i][j] in grids){
                        return false
                    }
                    else {
                        grids[board[i][j]] = 1
                    }
                }
            }
        }
    }
    return true
};