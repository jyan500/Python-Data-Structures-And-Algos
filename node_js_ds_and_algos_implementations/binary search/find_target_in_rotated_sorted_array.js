class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        /*
        using binary search,
        find the inflection point where
        at i, the element is smaller than the element at index 0,
        we keep searching the left until this is no longer the case,
        since in a rotated sorted array, the inflection point would be the smallest number
        where nums[0] > nums[i], and nums[nums.length-1] > nums[i]

        after that, we run binary search on both sides of the inflection point
        to figure out the index of the target

        Time: O(LogN)
        Space: O(1)
        */

        // find inflection point
        let l = 0
        let r = nums.length - 1
        let inflection = 0
        while (l <= r){
            let mid = l + Math.floor((r-l)/2)
            // if the midpoint number is less than the element at index 0,
            // that means we are in the "rotated portion", so we can
            // get as close to the inflection point by searching the left
            if (nums[mid] < nums[0]){
                inflection = mid
                r = mid - 1
            }
            else {
                l = mid + 1
            }
        }
        
        const binarySearch = (l, r) => {
            while (l <= r){
                let mid = l + Math.floor((r-l)/2)
                // need to search the right to find a bigger number
                // if the current is less than the target
                if (nums[mid] === target){
                    return mid
                }
                if (nums[mid] < target){
                    l = mid + 1
                }
                else {
                    r = mid - 1
                }
            }
            return -1
        }
        // run binary search on both sides of the inflection
        const left = binarySearch(0, inflection)
        const right = binarySearch(inflection, nums.length-1)
        
        if (left !== -1){
            return left
        }
        else if (right !== -1){
            return right
        }
        return -1
    }
}
