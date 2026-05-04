class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[][]}
     */
    fourSum(nums, target) {
        /*
        three sum, but hold two elements constant,
        then perform the loop with 2 pointers 
        starting from opposite ends and going inwards, until the sum
        equals the target.
        If the sum is greater than the target, move the right pointer inwards
        if the sum is less than the target, move the left pointer inwards 
        */
        nums.sort((a,b)=>{
            if (a < b){
                return -1
            }
            else if (a > b){
                return 1
            }
            return 0
        })
        let res = new Set()
        for (let i = 0; i < nums.length; ++i){
            for (let j = i+1; j < nums.length; ++j){
                let l = j+1
                let r = nums.length-1
                while (l < r){
                    let sum = nums[l] + nums[r] + nums[i] + nums[j]
                    // continue the loop as you may find more results inside the loop
                    if (sum === target){
                        res.add(`${nums[i]},${nums[j]},${nums[l]},${nums[r]}`)
                        ++l
                        --r
                    }
                    else if (sum < target){
                        ++l
                    }
                    else {
                        --r
                    }
                }
            }
        }
        return [...res].reduce((acc,string)=>{
            acc.push(string.split(","))
            return acc
        }, [])
    }
}
