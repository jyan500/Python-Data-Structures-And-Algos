class Solution {
    /**
     * @param {number[]} heights
     * @return {number[]}
     */
    findBuildings(heights) {
        /* 
        O(N) Time
        O(N) Space
        Suffix
        if we precalculate the "max" number we've seen so far from the right,
        this will tell us whether at a given index, if there's any value that
        would "block the way" that we've seen previously
        This is a similar concept to the trapping rain water problem
        */
        let suffix = [...heights]
        for (let i = suffix.length - 2; i >= 0; --i){
            suffix[i] = Math.max(suffix[i+1], suffix[i])
        }
        // the extra element is to account for the fact that
        // the rightmost element has nothing to the right of it,
        // so heights[i] > suffix[i+1] would be true for the last element
        suffix.push(0)
        let res = []
        for (let i = 0; i < suffix.length - 1; ++i){
            if (heights[i] > suffix[i+1]){
                res.push(i)
            }
        }
        return res
    }
}
