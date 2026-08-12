class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        /* 
        Revisited 6/12/2026
        note that the edges (either index 0 and length - 1)
        cannot trap any water, since before index 0 and after length - 1
        are not "walls" that can trap water 

        prefix and suffix
        for prefix, at a given index, figure out the
        max height to the left
        for suffix, at a given index, figure out the 
        max height to the right

        Once you have both,
        you can then take the MIN() between the two, as the minimum
        is the threshold where the water can be trapped
        i.e 
        |   
        |   |
        | _ |

        min(3, 2) means water can only be trapped up to height 2

        this represents the max water that can be trapped at i

        repeat this process for each index and then sum the results
        to get the max water that can be trapped between all the bars
        */
        let prefix = [...height]
        let suffix = [...height]
        let res = Array(height.length).fill(0)

        for (let i = 1; i < prefix.length; ++i){
            prefix[i] = Math.max(prefix[i-1], prefix[i])
        }
        for (let i = suffix.length-2; i >= 0; --i){
            suffix[i] = Math.max(suffix[i+1], suffix[i])
        }

        // note that because there's no wall on the left,
        // for the prefix, index 0 always start at max height 0
        prefix[0] = 0

        // for suffix, index of length - 1 always starts at 0 since
        // there's no wall to the right
        suffix[suffix.length-1] = 0

        for (let i = 1; i < height.length-1; ++i){
            // calculate the area
            let thresholdHeight = Math.min(prefix[i],suffix[i])
            // subtract the actual height from the max to get the area for this
            // particular column
            let area = thresholdHeight - height[i]
            if (area > 0){
                res[i] = area
            }
        }
        return res.reduce((acc, obj) => acc + obj, 0)
    }
}

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