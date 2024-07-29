/**
 * @param {number[]} nums
 * @return {number}
 */
var specialArray = function(nums) {
    /*
    Neetcode Prefix solution
    https://www.youtube.com/watch?v=Z51jYCeBLVI
    Two Pass Solution:
    In the brute force, for example in the example below with [3, 5],
    if you asked, at 2, are there exactly 2 elements that are >= 2, 
    and then tried calculating for 1, you can see that the amount of elements >= 1
    is actually the amount of elements === 1 PLUS the amount of elements >= 2
    
    Therefore, we can avoid repeated work by using a prefix array to track the counts of elements
    that we've already seen
    
    1,2,4,5,6
    
    create an array like so with nums.length+1, notice the one extra element because we want the numbers to represent
    0 1 2 3 4 5, similar to in the brute force where we check everything from 0 ... 5
    
    [0,0,0,0,0,0]
    
    for each element in nums...
    1st iteration:
    1 < 5, so 1
    count[1]++
    [0,1,0,0,0,0]
    
    2nd iteration
    2 < 5, so count[2]++
    [0,1,1,0,0,0]
    
    3rd iteration
    4 < 5, so count[4]++
    [0,1,1,0,1,0]
    
    4th iteration
    5 === 5, so we use count[5] instead as the length of nums is 5
    [0,1,1,0,1,1]
    
    5th iteration
    6 >= 5, so we use count[5] instead as the length of nums i 5
    [0,1,1,0,1,2]
    
    then, we iterate in reverse, notice that it starts at i = nums.length (instead of length - 1) and decrements
    we apply the prefix sum by storing the current sum in the variable "totalRight"
    if i === totalRight, that means there are i amount of elements that are >= i, so we return i
    if we go through the whole loop, return -1 since this means there's no element that meets the condition
    */
    // this is meant to be an array that holds the counts of each element in nums
    // [1, len(nums)+1]
    let count = []
    for (let i = 0; i < nums.length+1;++i){
        count.push(0)
    }
    for (let n of nums){
        // if an element is >= nums.length (the largest number), store the count in the last position
        let index = n < nums.length ? n : nums.length
        ++count[index]
    }
    let totalRight = 0
    for (let i = nums.length; i >= 0; --i){
        totalRight += count[i]
        if (totalRight === i){
            return i
        }
    }
    return -1
    /*
    Brute Force solution 
    O(N^2)
    max possible is nums.length, cannot have more elements than that
    [3, 5]
    starting at 0, are there exactly 0 elements that are >= 0?
    starting at 1, are there exactly 1 elements that are >= 1?
    starting at 2, are there exactly 2 elements that are >= 2?
    */
    // for (let i = 0; i <= nums.length; ++i){
    //     let count = 0
    //     for (let j = 0; j < nums.length; ++j){
    //         if (nums[j] >= i){
    //             ++count
    //         }
    //     }
    //     if (count === i){
    //         return i
    //     }
    // }
    // return -1
};