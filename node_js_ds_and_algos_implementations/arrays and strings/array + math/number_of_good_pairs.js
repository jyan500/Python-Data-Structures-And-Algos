/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    /*
    O(N^2) time solution is two for loops
    ensures that i < j
    for each i
        for each j = i + 1 ...
        
    */
    // let count = 0
    // for (let i = 0; i < nums.length; ++i){
    //     for (let j = i + 1; j < nums.length; ++j){
    //         if (nums[i] === nums[j]){
    //             ++count
    //         }    
    //     }
    // }
    // return count
    /*
    O(N) time, O(N) space solution
    keep track of count
    math: combinations are defined as n * (n-1), where n is the total count of a given element. Because we're counting pairs, divide the total amount by 2
    */
    let counter = {}
    for (let num of nums){
        if (num in counter){
            ++counter[num]
        }
        else {
            counter[num] = 1
        }
    }
    let count = 0
    for (let num in counter){
        let n = counter[num]
        let totalPairs = (n * (n-1))/2
        count += totalPairs
    }
    return count
};