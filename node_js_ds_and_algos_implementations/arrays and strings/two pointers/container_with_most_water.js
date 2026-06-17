// https://leetcode.com/problems/container-with-most-water/

class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        /*
        Revisited 6/17/2026
        two pointer starting from opposite sides, because
        we want to optimize for the largest width, then at each l and r, 
        heights[l] and heights[r] to be as large as possible

        1 7 2 5 4 7 3 6

        l = 0, r = 7
        heights[l] is 1, heights[r] is 6, so we are bounded by
        the smaller height here. height = 1, width = 7 - 0 = 7
        area of 7, at this point, this is our current max

        since heights[l] < heights[r], move only the left pointer inwards

        l = 1, r = 7
        heights[l] is now 7, and heights[r] = 6, we are bounded by the smaller height,
        so height = 6, width = 7 - 1= 6, area of 36, current max
        */
        let l = 0 
        let r = heights.length - 1
        let maxArea = 0
        while (l <= r){
            // calculate width * height to get the area
            maxArea = Math.max(Math.min(heights[l], heights[r])*(r-l), maxArea)
            if (heights[l] < heights[r]){
                ++l
            }
            else {
                --r
            }
        }
        return maxArea
    }
}

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let i = 0
    let j = height.length - 1
    let maxArea = 0
    while (i < j){
        // the container is always bounded by the smaller height
        let h = Math.min(height[i], height[j])
        let w = j - i
        maxArea = Math.max(h * w, maxArea)
        // if the height on the right is smaller, we are bounded by the right height,
        // so continue iterating to find a bigger height on the right
        if (height[j] < height[i]){
            --j
        }
        // if the height on the right is larger, we are bounded by the left height,
        // so continue iterating to find a bigger height on the left 
        else if (height[j] > height[i]){
            ++i
        }
        else{
            --j
            ++i
        }
    }
    return maxArea
};