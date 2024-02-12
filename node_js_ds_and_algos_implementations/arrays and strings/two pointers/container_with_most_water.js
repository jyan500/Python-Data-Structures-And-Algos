// https://leetcode.com/problems/container-with-most-water/
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