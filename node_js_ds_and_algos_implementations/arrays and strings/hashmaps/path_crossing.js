/**
 * @param {string} path
 * @return {boolean}
 */
/* 
https://leetcode.com/problems/path-crossing/submissions/
*/
var isPathCrossing = function(path) {
    let directions = {"S": [-1, 0], "N": [1, 0], "E": [0, 1], "W": [0, -1]}
    let visited = new Set()
    visited.add(`0,0`)
    let i = 0
    let j = 0
    for (let p of path){
        let [x, y] = directions[p]
        i = i + x
        j = y + j
        if (visited.has(`${i},${j}`)){
            return true
        }
        visited.add(`${i},${j}`)
        
    }
    return false
};