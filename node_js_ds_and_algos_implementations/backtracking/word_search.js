/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
/* 
DFS within a 2-D array:
1) You can use an array of objects to keep track of directions instead of using a list 
of tuples like in python
2) visited can store the indices i, j in a string like so `${i},${j}`

Time Complexity: O(N*M) * O(N+M)
Space Complexity: O(N*M) (potentially for the visited set)

Approach:
1) Iterate through 2-D array, looking for a starting cell (i, j) that contains the character at word[0]
2) At this (i, j), begin running DFS, iterating in four directions (up, down, left, right)
	- within our DFS, we track the current index of the word, and while iterating in four directions,
	we want to choose the path which has the next character that we're looking for
	- we also keep track of a visited set to make sure we don't revisit the same cell during a given path
	- once we find a direction to go in, we call DFS again, also making sure that it's in bounds of the 2-D array,
	and that we haven't visited it already. We increment word index + 1 to show that we're looking for 
	the next character in word.
3) Our base case: once we reach wordIndex >= word.length, that means that we must have found the word,
so return true
4) If we didn't find out word and there's no other paths we can go down, the DFS will backtrack to a previous case.
If so, we need to make sure to pop out the i, j that we just visited from our visited set, since we may potentially
backtrack into a previous cell, and then go down a new path that "revisits" these cells.
5) If our DFS returns true, we can just return true repeatedly to avoid any un-necessary calls.
*/
var exist = function(board, word) {
    var inBounds = function(i, j, m, n){
        return 0 <= i && i < m && 0 <= j && j < n
    }
    var dfs = function(i, j, wordIndex, visited){
        let directions = [{x: 0,y: 1}, {x: 0, y:-1}, {x: 1, y: 0}, {x:-1, y: 0}]
        if (wordIndex >= word.length){
            return true
        }
        let flag = false
        for (let d of directions){
            let {x, y} = d
            let newX = i + x
            let newY = j + y
            if (inBounds(newX, newY, board.length, board[0].length) && board[newX][newY] === word[wordIndex] && !visited.has(`${newX},${newY}`)){
                visited.add(`${newX},${newY}`)
                if (dfs(newX, newY, wordIndex+1, visited)){
                    return true
                }
                // if the DFS goes down the wrong path, when backtracking to each recursive call, you need to pop
                // from delete so that once DFS goes down a new path, it can potentially revisit these cells,
                // if you didn't pop these, the new path would not be able to visit these cells again.
                visited.delete(`${newX},${newY}`)
            }
        }
        return false
    }
    let m = board.length
    let n = board[0].length
    for (let i = 0; i < m; ++i){
        for (let j = 0; j < n; ++j){
            if (board[i][j] === word[0]){
                let visited = new Set()
                visited.add(`${i},${j}`)
                if (dfs(i, j, 1, visited)){
                    return true
                }
            }
        }
    }
    return false
    
};