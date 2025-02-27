'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Revisited 2/27/2025
        1) sort the numbers
        2) Do an initial loop through all numbers:
            hold the first element constant, and then apply
            the two pointer strategy where the pointers move 
            inwards from opposite ends
            if the first element + (the two pointers) is greater than 0,
            you have to move the right pointer to decrease the overall
            value since you're now adding a smaller number
            if its less than, you need to move the left pointer
            to get a bigger number

        """
        nums.sort()
        resSet = set()
        for i in range(len(nums)-1):
            l = i + 1
            r = len(nums)-1
            while (l < r):
                res = nums[i] + nums[l] + nums[r]
                if res > 0:
                    r -= 1
                elif res < 0:
                    l += 1
                else:
                    resSet.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
        return list(resSet)
            

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


            