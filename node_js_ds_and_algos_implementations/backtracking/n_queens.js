/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    /*
    queens can move diagonally in all four directions
    and horizontally in all four directions
    
    brute force:
    example 4 x 4 board
    let's say you place a queen at position (0, 0), 
    how many positions are left to place queens without being
    in attack by the queen we just placed at (0, 0)?
    
    positions that we cannot place is anything directly to the right, directly below or diagonally right,
    once we place a queen, mark the board to show all the places where a queen cannot be placed. 
    
    The key is that after we place a queen, we cannot place another queen in the same row, so we pass in i + 1 into the following recursive call
    
    for example:
    Q * * *
    * * * *
    * * * *
    * * * *
    
    Once we place a queen, we know we can't place a queen in the following areas, so we mark them with #
    Q # # #
    # # * *
    # * # *
    # * * #
    
    In the next recursive call, we would be able to place a queen at
    (1, 2), that would be one recursive path we could take,
    we could also place it at (1, 3), and so on...
    
    Doing this, we find out that we can only place 3 queens.
    
    After each recursive call finishes, we need to "undo" the work
    by unmarking all the "#" in the board when we placed 
    the queen during the recursive call, since these ranges are now available to potentially place a queen
    
    Time Complexity:
    It's certainly exponential, but not sure to what degree. My guess here is O(N^N), because given a row of N spots, we can come up with N different ways to place the queen for each spot 
    
    Space Complexity:
    O(N^2) we're making copies of the board at one point
    */
    const directions = [
        {x: 0, y: 1},
        {x: 0, y: -1},
        {x: 1, y: 0},
        {x: -1, y: 0},
        {x: 1, y: 1},
        {x: 1, y: -1},
        {x: -1, y: 1},
        {x: -1, y: -1}
    ]
    let board = []
    for (let i = 0; i < n; ++i){
        let inner = []
        for (let j = 0; j < n; ++j){
            inner.push(".")
        }
        board.push(inner)
    }
    let res = []
    let visited = new Set()
    var inBounds = function(x, y){
        return x >= 0 && x < n && y >= 0 && y < n
    }
    var search = function(i1, numQueens){   
        let coordinates = []
        let queenPosition = {i: 0, j: 0}
        if (numQueens === n){
            // take a "snapshot" of the board in this state
            let copy = [...board]
            let boardString = ""
            for (let i = 0; i < n; ++i){
                // you need to add /g to do a global replacement, otherwise
                // it just replaces the first character
                let parsed = copy[i].join("").replace(/#/g, ".")
                boardString += parsed
                copy[i] = parsed
            }
            if (!visited.has(boardString)){
                visited.add(boardString)
                res.push(copy)
            }
            return
        }
        for (let i = i1; i < n; ++i){
            for (let j = 0; j < n; ++j){
                // if empty spot
                if (board[i][j] === "."){           
                    // try placing a queen at i, j
                    board[i][j] = "Q"
                    queenPosition = {...queenPosition, i: i, j: j}
                    // find out all the positions on the board
                    // where the queen would be attacking, and thus
                    // cannot be placed. Indicate this with "#"
                    for (let d of directions){
                        let {x, y} = d
                        let newX = i
                        let newY = j
                        while (true){
                            newX = newX + x
                            newY = newY + y
                            if (inBounds(newX, newY)){
                                if (board[newX][newY] !== "#" && board[newX][newY] !== "Q"){
                                    coordinates.push({x: newX, y: newY})
                                    board[newX][newY] = "#"
                                }
                            }
                            else {
                                break
                            }
                        }
                    }
                    search(i+1, numQueens+1)  
                    // if the recursion finishes, we have to "reverse"
                    // all the changes we just made to the board
                    // to make space for new paths in the recursion       
                    // search here
                    for (let c of coordinates){
                        let {x, y} = c
                        board[x][y] = "."
                    }
                    // undo the queen's position
                    board[queenPosition.i][queenPosition.j] = "."
                }
            }
        }
    }
    
    search(0, 0)
    return res
    
};