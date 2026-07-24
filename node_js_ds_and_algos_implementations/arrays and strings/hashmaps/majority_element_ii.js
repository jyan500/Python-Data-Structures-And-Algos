class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    majorityElement(nums) {
        let counter = new Map()
        for (let i = 0; i < nums.length; ++i){
            counter.set(nums[i], (counter.get(nums[i]) || 0) + 1)
        } 
        let res = []
        for (const [key, value] of counter.entries()){
            if (value > Math.floor(nums.length/3)){
                res.push(key)
            }
        }
        return res
    }
}
