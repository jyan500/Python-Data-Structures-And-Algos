'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
'''

def threeSumBruteForce(self, nums: List[int]) -> List[List[int]]:
	## O(NLogN) + O(N^3), a brute force solution (this solution times out on leetcode)
	triplets = []
	nums.sort()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                a = nums[i] + nums[j] + nums[k]
                if (a == 0 and [nums[i], nums[j], nums[k]] not in triplets):
                    triplets.append([nums[i], nums[j], nums[k]])
    return triplets

def threeSum(self, nums: List[int]) -> List[List[int]]:
	## O(N^2) solution, using two pointers and sorting the initial list
	triplets = []
	nums.sort()
    for i in range(len(nums)):
    	left = i+1
    	right = len(nums) - 1
        while (left < right):
        	s = nums[i] + nums[left] + nums[right]
        	if (s == 0 and [nums[i], nums[left], nums[right]] not in triplets):
        		triplets.append([nums[i], nums[left], nums[right]])
        	elif (s > 0):
        		right-=1
        	else:
        		left+=1
    return triplets


            