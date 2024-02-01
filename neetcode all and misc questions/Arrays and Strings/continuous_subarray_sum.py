class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    	"""
    	https://leetcode.com/problems/continuous-subarray-sum/
    	Neetcode Solution:
    	https://www.youtube.com/watch?v=OKcrLfR-8mE
		
		1) The key trick to this problem is that we can keep a hashmap that 
		stores the value of prefix sum % k as the key and the index as the value

		- The reasoning is that if we see the same remainder twice,
		that means that while we were adding numbers to our prefix sum,
		we must've added numbers that were a multiple of K.

		2) We store the index because we need to make sure that the subarray is at least length of 2
		3) We also initialize the hash map with {0: -1} to avoid an edge case where index 0 in the array
		is a multiple of K. 

		Example:

		23 3 2 2 2. . . , k = 6
		
		i = 0
		23 % 6 = 5 

		Map = {0: -1, 5: 0}
	
		i = 1
		23 + 3 = 26, 26 % 6 = 2

		Map = {0: -1, 5: 0, 2: 1}
		
		i = 1
		26 + 2 = 28, 28 % 6 = 4

		Map = {0: -1, 5: 0, 2: 1, 4: 2}
		
		i = 3
		28 + 2 = 30, 30 % 6 == 0

		Map = {0: -1, 5: 0, 2:1, 4: 2, 6: 3}

		Here, we notice that 0 already exists in the hashmap at index -1

		and this makes sense because the subarray that we've added so far
		is divisible by 6, so this is saying that anything past index -1 (starting at index 0)
		is divisible by 6, which is our answer

		3 - (-1) = 4, this is a subarray of length 4, which is greater than 2

    	"""
        # brute force solution O(N^2)
        # for i in range(len(nums)):
        #     curSum = nums[i]
        #     for j in range(i+1, len(nums)):
        #         curSum += nums[j]
        #         if curSum % k == 0:
        #             return True
        # return False
        remainderMap = {0: -1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            remainder = prefix % k
            if remainder in remainderMap:
                j = remainderMap[remainder]
                # make sure the subarray is at least length 2
                if i - j >= 2:
                    return True
            else:
                remainderMap[remainder] = i
        return False