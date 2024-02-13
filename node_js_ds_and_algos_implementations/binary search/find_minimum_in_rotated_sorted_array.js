/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    /*
    in a normal sorted array:
    you'd expect the elements to be strictly increasing going to the right,
    and strictly decreasing going to the left
    in rotated sorted array however:
    for one element, the element to the right will have a decreased value
    , and the element on the left will have an increased value, this is where the "rotation" point was
    
    for example:
    4 5 6 7 0 1 2 3
    the rotation point is where the value of 0 was, since it goes
    from value of 7 to value of 0
    
    Therefore, to find the minimum value, we do a binary search where
    given mid, if right side is less than mid,  we should do a binary search on this side since in a normal sorted array, the right side should never be less than the mid
   if the right side is greater than mid though, that means the right side has the "proper" sorting order, so the reflection point must be on the left side
    
    */
    const helper = (l, r, nums) => {
        let mid = l + Math.floor((r-l)/2)
        if (l >= r){
            return nums[l]
        }
        else if (nums[mid] > nums[r]){
            return helper(mid+1, r, nums)
        }
        else{
            // unlike regular binary search,
            // make sure we include mid as a right most,
            // since there's an edge case where the mid
            // may already be our minimum, so we have to include it
            // in our search space.
            return helper(l, mid, nums)
        }
    }
    return helper(0, nums.length-1,nums)
};