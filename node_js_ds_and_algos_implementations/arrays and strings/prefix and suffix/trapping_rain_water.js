// https://leetcode.com/problems/trapping-rain-water/
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    // suffix, iterate from back, we only need to look at the element before
    // since it's cumulative
    let maxHeightsRight = height.map(x=>x)
    // prefix, iterate from front, we only need to look at the element before
    // since it's cumulative
    let maxHeightsLeft = height.map(x=>x)
    for (let i = height.length-2; i >= 0; --i){
        maxHeightsRight[i] = Math.max(maxHeightsRight[i+1], maxHeightsRight[i])
    }
    for (let i = 1; i < height.length; ++i){
        maxHeightsLeft[i] = Math.max(maxHeightsLeft[i-1], maxHeightsLeft[i])
    }
    let amounts = height.map(x=>x)
    // the amount of rain water that can be trapped at a given index i is the min between the max height to the left
    // and the max height to the right, subtracted from the current height at index i
    // for example, i = 1 which is 0, if we look at the max height to the left at i = 0, its 1, and to the right at i = 2, it's 2
    // so min(2, 1) = 1, and 1 - 0 = 1, so we can trap one rain water
    // if the amount ends up negative, since we can't trap negative rain water, set this to 0
    for (let i = 0; i < amounts.length; ++i){
        // left most edge, there's no left
        let amt = 0
        if (i === 0){
            amt = Math.min(0, maxHeightsRight[i+1]) - height[i] 
        }
        // right most edge
        else if (i === amounts.length - 1){
            amt = Math.min(0, maxHeightsLeft[i-1]) - height[i]
        }
        else {
            amt = Math.min(maxHeightsRight[i+1], maxHeightsLeft[i-1]) - height[i]
        }
        amounts[i] = amt > 0 ? amt : 0
    }
    return amounts.reduce((amt, acc) => acc += amt, 0)
};