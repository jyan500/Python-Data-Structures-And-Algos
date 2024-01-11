"""
https://leetcode.com/problems/subarray-sum-equals-k/
https://www.youtube.com/watch?v=fFVZt-6sgyo&ab_channel=NeetCode

Prefix Sum Method 
https://www.youtube.com/watch?v=fFVZt-6sgyo&ab_channel=NeetCode
O(N) Time and O(N) space
1) keep a hashmap containing the prefix sum and the count, where the prefix sum
is the current sum - K 
2) the count will determine the amount of sub arrays that sum to K,
because if you were to "remove" these prefix sums, this would create the subarrays
that sum to k (see example below)
3) As an edge case, we always keep the prefix sum 0 with count of 1 in the case
of list of length == 1, there'd only be one subarray in that case 

Example:
nums = [1, -1, 1, 1, 1, 1]
k = 3
Find all subarrays that sum to 3

counter = {0: 1}
curSum = 0
res = 0

1st iteration (i = 0)
---------------------
curSum = 0 + 1 = 1
prefixSum = 1 - 3 = -2

prefixSum is not in counter
save curSum into counter
counter = {0: 1, 1: 1}

2nd iteration (i = 1)
---------------------
curSum = 1 + -1 = 0
prefixSum = 0 - 3 = -3

prefixSum is not in counter
save curSum into counter
counter = {0: 2, 1: 1}

3rd iteration (i = 2)
---------------------
curSum = 0 + 1 = 1
prefixSum = 1 - 3 = -2

prefixSum is not in counter
save curSum into counter
counter = {0: 2, 1: 2}

4th iteration (i = 3)
----------------------
curSum = 1 + 1 = 2
prefixSum = 2 - 3 = -1

prefixSum is not in counter
save curSum into counter
counter = {0: 2, 1:2, 2:1}

5th iteration (i = 4)
-----------------------
curSum = 2 + 1 = 3
prefixSum = 3 - 3 = 0

prefixSum IS in counter!
increment res by 2 (since the value of key 0 is 2) = 2

Notice that in the nums array
[1, -1, 1, 1, 1, 1]
these are the two subarrays that are summing to k:
[1, -1, 1, 1, 1, 1]
        ^-----^

[1, -1, 1, 1, 1, 1]
 ^------------^

as well as the 

save curSum into counter
counter = {0: 2, 1:2, 2:1, 3:1}

6th iteration (i = 5)
----------------------
curSum = 3 + 1 = 4
prefixSum = 4 - 3 = 1

prefixSum IS in counter!
increment res by 2 (since the value of key 1 is 2) = 4


Notice that in the nums array
[1, -1, 1, 1, 1, 1]
these are the two subarrays that are summing to k:
[1, -1, 1, 1, 1, 1]
           ^-----^

[1, -1, 1, 1, 1, 1]
    ^------------^

save curSum into counter
counter = {0: 2, 1:2, 2:1, 3:1, 4:1}

Done, return res = 4
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force O(N^2)
        # cur = 0
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         cur += nums[j]
        #         if cur == k:
        #             count += 1
        #     cur = 0
        # return count
        

        # prefix sum method
        counter = {0: 1}
        curSum = 0
        res = 0
        for i in range(len(nums)):
            curSum += nums[i]
            prefixSum = curSum - k
            if prefixSum in counter:
                res += counter[prefixSum]

            if curSum in counter:
                counter[curSum] += 1
            else:
                counter[curSum] = 1
        return res
            