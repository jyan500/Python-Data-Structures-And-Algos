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