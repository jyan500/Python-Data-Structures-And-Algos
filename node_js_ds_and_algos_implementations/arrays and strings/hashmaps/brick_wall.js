/**
 * @param {number[][]} wall
 * @return {number}
 */
var leastBricks = function(wall) {
    /*
        The idea is hashmap + reverse thinking + prefix sums:
        We can get the least amount of bricks crossed by counting the MAX amount of gaps,
        and then subtracting from the height
        
        for example, if wall.length = 6, and the amount of gaps = 4, min amount of bricks crossed is 2
        
        We can use a hashmap to count the amount of gaps.
        
        initialize hashmap with a dummy key of 0 and value 0. THIS IS IMPORTANT because it accounts for an edge
        case where there are no gaps present and there's only one brick on each level (i.e [[1], [1], [1]])
        
        iterate through rows and cols,
            initialize the current gap, which is the value of the first wall value (wall[i][0])
            if curGap in hashmap, increment else initialize to 1
            in order to determine where the next gap is, you have to take the current gap value, plus the next wall value
            curGap + wall[i][j+1], which is the prefix sum
        
        return wall.length - max value of hashmap

        Time Complexity:
        O(N*M) (needs to do nested loop to iterate through each level per wall)
        Space:
        O(M) (only space required is the total amount per level)

    */
    
    // initializing a dummy key of 0, and value 0 is important to avoid this edge case: [[1], [1], [1]], where
    // there's no gaps, and there's only one brick on each level. This way, you'd get 3 - 0 gaps, 3 bricks crossed.
    let countGap = {0:0}
    for (let i = 0; i < wall.length; ++i){
        let curGap = wall[i][0]
        for (let j = 0; j < wall[i].length-1; ++j){
            if (!(curGap in countGap)){
                countGap[curGap] = 1
            }
            else{
                ++countGap[curGap]
            }
            curGap = curGap + wall[i][j+1]
        }
    }
    let maxGaps = Math.max(...Object.values(countGap))
    return wall.length - maxGaps
};