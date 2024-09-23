/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    /*
    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
    elements are already sorted by asc
    get only the first two instances of each element in the nums array
    1) keep a counter of the amount of elements that appear more than 2 times, this
    is also the amount of placeholders we'll need
    2) if the previous element is the same, and the count is greater than 2, replace the element with a placeholder
    3) Loop through again and remove the placeholders
    4) The amount of elements returned should be the total of nums - numPlaceholders,
    as this indicates the amount of elements that have count > 2

    O(2N) Time
    O(1) Space
    */
    let previous = nums[0]
    let previousCount = 1
    let i = 1 
    let N = nums.length
    while (i < N){
        if (previous === nums[i]){
            previousCount++
            if (previousCount >= 3){
                nums[i] = "-"
            }
        }
        else {
            previous = nums[i]
            previousCount = 1
        }
        ++i
    }
    let j = 0
    let amt = 0
    while (j < N){
        if (nums[j] === "-"){
            nums.splice(j, 1)
            amt++
            /* you need to continue here, otherwise once you remove an element,
            the index will shift over by 1, so if there's consecutive placeholders, one of them will be 
            missed. For example:
            [-, -, 1, 2]
            i = 0
            once - is removed, nums = [-, 1, 2], if incrementing i to be 1, 
            i is now pointing at nums[1] = 1 instead of -, which is nums[0] in the new array 
            */
            continue
        }
        ++j
    }
    return N - amt
};