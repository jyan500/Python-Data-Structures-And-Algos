/**
 * @param {number[][]} grid
 * @return {number}
 */
var gridGame = function(grid) {
    /*
    see python version for complete explanation
    basically there are only N different possible paths for robot 1 to take,
    it can either go down at i or go left.
    
    i.e N = 4
    
    - - - -
          |
    - - -
        |
         -
    - -
      |
      - -
    -
    |
    - - - -
    
    Using prefix sums, this tells us how much robot 2 would get if robot 1 went down a particular path
    */
    let N = grid[0].length
    let pre1 = grid[0].map((x) => x)
    let pre2 = grid[1].map((x) => x)
    
    for (let i = 1; i < N; ++i){
        pre1[i] = pre1[i-1]+pre1[i]
        pre2[i] = pre2[i-1]+pre2[i]
    }
    
    let topTotal = grid[0].reduce((acc, x) => acc + x, 0)
    let res = Number.POSITIVE_INFINITY
    for (let i = 0; i < N; ++i){
        // if robot 1 goes down this column at i, robot 2 would then gain the sum of the rest of the numbers in this row
        let top = topTotal - pre1[i]
        // if robot 1 goes down this column, robot 2 would only be able to gain points to the left of this column
        // since robot1 would've taken the remainder of the bottom and set all the remaining numbers to 0 in this row (since the robot1 can only go right at this point)
        let bottom = i > 0 ? pre2[i-1] : 0 
        res = Math.min(res, Math.max(top, bottom))
    }
    return res
};