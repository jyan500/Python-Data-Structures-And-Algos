/*
Review this video by Knapsack for the explanation
https://www.youtube.com/watch?v=6poxiip7sBY

The key is reverse thinking (prefix sum) + hashmaps: 
when keeping track of the current sum,
if currentSum - k is in our hashmap, this means this subarray of currentSum - k has been calculated before.
This helps us because the subarrays between the subarrays that add to currentSum - k represent the actual
subarrays that target to k that we're interested in.

See 7:39 on the linked youtube video,

1 1 2 6 -6 -2 2 2 , k = 4

for example, at the end, currentSum = 6
6 - k (where k is 4) is equal to 2

occur = {
	0: 1,
	1: 1,
	2: 2,
	4: 3,
	10: 1,
	6: 1	
}

There are 2 instances of subarrays that sum to 2. Therefore, by definition,
because 6 - 2 = 4, there must ALSO be 2 subarrays that sum to 4 

1 1 2 6 -6 -2 2 2 
- - * *  *  * * *

the subarray indicated by the dashes sums to 2. So the remainder of the array indicated by * sums to 4 since
the current sum is 6

1 1 2 6 -6 -2 2 2 
- - - -  -  - * *

the subarray indicated by the dashes sums to 2. So the remainder of the array indicated by * sums to 4.

So if current sum - k exists, occur[current sum - k] would also correspond to
the same amount of subarrays that sum to k

O(N) Time
O(N) Space

*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let occur = {
        0: 1
    }
    let counter = 0 
    let currentSum = 0
    for (let i = 0; i < nums.length; ++i){
        currentSum += nums[i]
        if (currentSum - k in occur){
            counter += occur[currentSum - k]
        }
        if (currentSum in occur){
            ++occur[currentSum]    
        }
        else {
            occur[currentSum] = 1
        }
    }
    return counter
};
