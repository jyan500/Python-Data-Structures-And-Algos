/**
 * @param {number[]} nums
 * @return {number}
 */
/*
Approach:
since we're only concerned with the length of the longest increasing subsequence, rather than the actual subsequence itself, we
keep track of a length, and when we see a number that is greater than previous, we increase the length. There's also the option to not 
count this in the subsequence, in that case, we'd just continue incrementing

Base Case: if we've reached the end of the list, the subsequence must've been at least a length of 1,
so return 1

With memoization:
O(N^2) time solution, since we still need to run an O(N) recursive search
on each number in the list. The memoization saves time within the recursive search
by cutting the time to O(N) instead of exponential 

Space: O(N)

Example:
[10, 14, 11, 12]

1st call:
start = 0
end = 0
nums[end] is not greater than nums[start]
length2 = search(start, end+1)

2nd call
start = 0
end = 1
nums[end] > nums[start]
len = search(end, end+1) + 1

3rd call
start = 1
end = 2
nums[2] is not greater than nums[1]
length2 = search(start, end+1)

4th call
start = 1
end = 3
nums[3] is not greater than nums[1]

5th call
start = 1
end = 4

base case reached, 4 >= N, returns 1

Back to the 4th call
start = 1
end = 3
Math.max(1, 1) = 1
returns 1

Back to the 3rd call
start = 1
end = 2
Math.max(1, 1) = 1
returns 1

Back to the 2nd call
start = 0
end = 1
len = 1 + 1 = 2
try the second route

length2 = search(start, end+1)

6th call
start = 0
end = 2
nums[2] > nums[0], 
len = search(end, end+1)+1

7th call
start = 2
end = 3
nums[3] > nums[2]
len = search(end, end+1)+1

8th call
start = 3
end = 4
base case reached (4 >= N)
returns 1

back to 7th call
start = 2
end = 3
len = 1 + 1 = 2

back to 6th call
start = 0
end = 2
len = 2 + 1 = 3

try 2nd route
length2 = search(start, end+1)

7th call
start = 0
end = 3
nums[3] > nums[0]
len = search(end, end+1)+1

8th call
start = 0
end = 4
base case reached (4 >= N), returns 1

back to 7th call
start = 0
end = 3
len = 1 + 1 = 2

it'll try 0 and 4, but won't work and will return 1, at this point
Math.max(2, 1) = 2, so return 2

back to 6th call
start = 0
end = 2
len = 3
length2 = 2
Math.max(3, 2) = 3

back to 2nd call
length2 = 3
len = 2 
Math.max(2, 3) = 3

back to 1st call
Math.max(1, 3) = 3

returns 3 here

In the for loop, we now try the starting index at 1
this is where the memo object comes in, since we've already 
calculated the max that can be reached at 1 (which is 1), we can simply just return 1

same with the other indices i = 2, i = 3, their answers are 2 and 1 respectively,
none of which are larger than 3

For another case like though
[11, 9, 10, 12]
we'd need this for loop in order to consider 9 as a starting point, otherwise,
since we start at 11, we'd skip 9 and 10 and consider 12 (for a length of 2)

in the loop when i = 1,
If we try starting from 9 here, we'd calculate 3 which is our final answer.

*/
var lengthOfLIS = function(nums) {
    let N = nums.length
    let memo = {}
    var search = function(start, end, i) {
        // base case, if we've reached the end, the length of the subsequence was at least 1, so return 1
        if (end >= N){
            return 1
        }
        if (start in memo){
            return memo[start]
        }
        // if we find an increasing number, set the 
        // new start to be end
        let len = 1
        if (nums[end] > nums[start]){
            len = search(end, end+1)+1
        }
        // we also have the option of not choosing this number
        // to include in our subsequence and looking for a different increasing number, in this case we keep start the same, and increment end
        // we also want to find the max length between if we were to choose
        // the increasing element, or if we were to ignore it and find another one
        let length2 = search(start, end+1)
        let maxLength = Math.max(len, length2)
        // at this start index, store the length of the longest
        // increasing subsequence starting at this index
        memo[start] = maxLength
        return maxLength
    }
    let res = Number.NEGATIVE_INFINITY
    for (let i = 0; i < N; ++i){
        res = Math.max(res, search(i, i))
    }
    return res
};