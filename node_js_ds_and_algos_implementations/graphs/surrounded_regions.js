class Solution {
    /**
     * @param {character[][]} board
     * @return {void} Do not return anything, modify board in-place instead.
     */
    solve(board) {
        /*
        first, find all indices that are surrounded,
        so as long as the island does not have a cell that sits on the boundary,
        it's considered surrounded

        similar to number of islands using DFS:
        determine if a given cell forms an island, and if any cell
        in this island is on the boundary, if so, we ignore this island

        we will store the potential islands in a set consisting of their x,y coords

        My initial solution involves more extra memory and steps (having to store the
        surrounded regions directly, then determine whether they are on the border)

        *** Optimization - opposite thinking ***

        Rather than trying to store all islands, 
        we can just apply DFS to ONLY the islands that are on the boundary by
        starting the DFS on a cell that's on the boundary and also == "O"

        Then, we just temporarily set these values to "T" within the board
        to act as a "visited" set so we don't confuse these with the cells
        that are actually surrounded.

        By default, any remaining "O" is going to be surrounded since we covered
        all the cases where the "O" belongs to an island that touches the border.

        Therefore, we just set those to "X", and then flip all the remaining "T"'s
        back to 'O's again

        Time: O(N*M)
        Space: O(1)
        */
        let directions = [[0,1],[0,-1],[1,0],[-1,0]]
        const inBounds = (i, j) => {
            return 0 <= i && i < board.length && 0 <= j && j < board[0].length
        }
        const convertBoundaryIsland = (i, j) => {
            for (let [x,y] of directions){
                let newX = x + i
                let newY = y + j
                if (inBounds(newX,newY) && board[newX][newY] === "O"){
                    board[newX][newY] = "T"
                    convertBoundaryIsland(newX, newY)
                }
            }
        }

        // left and right boundary
        for (let i = 0; i < board.length; ++i){
            if (board[i][0] === "O"){
                board[i][0] = "T"
                convertBoundaryIsland(i, 0)
            }
            if (board[i][board[0].length-1] === "O"){
               board[i][board[0].length-1] = "T" 
               convertBoundaryIsland(i, board[0].length-1)
            }
        }
        // top and bottom boundaries
        for (let j = 0; j < board[0].length; ++j){
            if (board[0][j] === "O"){
                board[0][j] = "T"
                convertBoundaryIsland(0, j)
            }
            if (board[board.length-1][j] === "O"){
                board[board.length-1][j] = "T"
                convertBoundaryIsland(board.length-1, j)
            }
        }

        // loop through and find all "O"s that remain and convert them to X
        for (let i = 0; i < board.length; ++i){
            for (let j = 0; j < board[0].length; ++j){
                if (board[i][j] === "O"){
                    board[i][j] = "X"
                }
            }
        }

        for (let i = 0; i < board.length; ++i){
            for (let j = 0; j < board[0].length; ++j){
                if (board[i][j] === "T"){
                    board[i][j] = "O"
                }
            }
        }

        /* 
        initial, slower solution is to store all islands, then determine whether
        they sit on the border or not, then filter them out and set the values
        */
        // const search = (i, j, visited) => {
        //     for (let [x,y] of directions){
        //         let newX = x + i
        //         let newY = y + j
        //         if (inBounds(newX,newY) && board[newX][newY] === "O" && !visited.has(`${newX},${newY}`)){
        //             visited.add(`${newX},${newY}`)
        //             globalVisited.add(`${newX},${newY}`)
        //             search(newX,newY,visited)
        //         }
        //     }
        // }

        // // find all islands
        // for (let i = 0; i < board.length; ++i){
        //     for (let j = 0; j < board[0].length; ++j){
        //         if (board[i][j] === "O" && !globalVisited.has(`${i},${j}`)){
        //             let visited = new Set()
        //             visited.add(`${i},${j}`)
        //             search(i,j,visited)
        //             islands.push(visited)
        //         }
        //     }
        // }

        // // determine if any of the islands have cells that are on the boundary
        // let surrounded = []
        // for (let islandSet of islands){
        //     let isSurrounded = true
        //     for (let coord of islandSet){
        //         let [x, y] = coord.split(",")
        //         if (onBoundary(Number(x),Number(y))){
        //             isSurrounded = false
        //             break
        //         }
        //     }
        //     if (isSurrounded){
        //         surrounded.push(islandSet) 
        //     }
        // }

        // // convert all the surrounded islands' indices in place to "X"
        // for (let islandSet of surrounded){
        //     for (let coord of islandSet){
        //         let [x,y] = coord.split(",")
        //         board[x][y] = "X"
        //     }
        // }
    }
}

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