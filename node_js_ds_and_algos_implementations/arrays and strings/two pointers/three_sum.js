class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        /* 
        Three Sum with no extra memory to handle duplicates:
        Sorting the array,
        we can hold one element at i constant, and then perform two pointers
        search on the remaining elements starting from opposite ends,
        so then if we take nums[i] + nums[l] + nums[r], if its greater than 0,
        we decrease r, and if its less than 0, increase l
        
        To avoid duplicates, you need to apply checks in two different areas:
        the first one is when we pick the constant "i", we have to make sure that the previous value
        we chose is not the same as the current, otherwise, we continue

        The second is inside the inner while loop
        in order to prevent picking the same l value and r value, we need to increment until we see a value that's different from the previous,
        same with r

        Time: O(NLogN + N^2)
        Space: O(1)
        */
        nums.sort((a,b) => {
            if (a < b){
                return -1
            }
            else if (a > b){
                return 1
            }
            return 0
        })
        let res = []
        for (let i = 0; i < nums.length; ++i){
            // also need to skip i values that are the same so the "first" element
            // that's held constant doesn't cause duplicate triplets
            if (i > 0 && nums[i-1] === nums[i]){
                continue
            }
            let l = i+1
            let r = nums.length-1
            while (l < r){
                let total = nums[i] + nums[l] + nums[r]
                if (total < 0){
                    ++l
                }
                else if (total > 0){
                    --r
                }
                else {
                    res.push([nums[i], nums[l], nums[r]])
                    // in order to prevent duplicates, we need to skip past
                    // the values that are the same as the previous that we already used
                    while (l < r && nums[l] === nums[l+1]){
                        ++l
                    }
                    while (l < r && nums[r] === nums[r-1]){
                        --r
                    }
                    ++l
                    --r
                }
            }
        }
        return res
    }
}

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
	/*
	Sort the array first
	Similar concept to two ii w/ input array sorted,
	hold one element constant in the outer loop,
	and then in the inner while loop, use two pointers
	to get a sum including the constant element, the left
	and right pointer element.
	If the sum > 0, we need a smaller number, so --r
	if the sum < 0, we need a bigger number, so ++l
	if we've found a unique, add that to the set, but continue the 
	iteration, --r and ++l

	Time:
	O(NLogN + O(N^2))
	Space: O(N)

	*/
    let uniques = new Set()
    const sortKey = (a,b)=>{
        return a-b
    }
    nums.sort(sortKey)
    for (let i = 0; i < nums.length; ++i){
        l = i+1
        r = nums.length - 1
        while (l < r){
            let sum = nums[i] + nums[l] + nums[r]
            if (sum === 0){
                uniques.add(`${nums[i]},${nums[l]},${nums[r]}`)
                ++l
                --r
            }
            else if (sum < 0){
                ++l
            }
            else if (sum > 0){
                --r
            }
        }
    }
    let res = []
    for (let s of uniques){
        res.push(s.split(","))
    }
    return res
};